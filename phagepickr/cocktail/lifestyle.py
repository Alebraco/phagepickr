#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import shutil
import subprocess
import pandas as pd
from Bio import Entrez, SeqIO
from glob import glob

env = 'phagepickr-bacphlip'
BATCH = 200


def bacphlip_command():
    executable = os.environ.get('PHAGEPICKR_BACPHLIP') or shutil.which('bacphlip')
    if executable:
        return executable

    for manager in ('conda', 'mamba', 'micromamba'):
        if shutil.which(manager):
            envs = subprocess.run(f'{manager} env list', shell=True, capture_output=True, text=True)
            if env in envs.stdout:
                return f'{manager} run -n {env} bacphlip'
            
    print('BACPHLIP not found. Create the environment with "conda env create -f environment-bacphlip.yml"')
    return None


def lifestyle_genomes(accessions, filename):
    print(f'Fetching {len(accessions)} genome(s) for lifestyle prediction')
    seqs = []

    for start in range(0, len(accessions), BATCH):
        handle = Entrez.efetch(db='nucleotide', id = accessions[start:start + BATCH], rettype = 'fasta', retmode = 'text')
        for record in SeqIO.parse(handle, 'fasta'):
            seqs.append(record)
        handle.close()

    with open(filename, 'w') as file:
        SeqIO.write(seqs, file, 'fasta')

    return filename


def run_bacphlip(input_file, command):
    output_file = f'{input_file}.bacphlip'
    # BACPHLIP will not overwrite, so clear the results of any previous run
    for old in glob(f'{input_file}.*'):
        shutil.rmtree(old) if os.path.isdir(old) else os.remove(old)

    print(f'Running lifestyle prediction: {input_file}')
    bacphlip_command_line = f'{command} -i {input_file} --multi_fasta'
    result = subprocess.run(bacphlip_command_line, shell=True, capture_output = True)

    if result.returncode == 0 and os.path.exists(output_file):
        print('> Lifestyle prediction performed successfully')
        return output_file
    else:
        print('Error predicting lifestyle')
        print(bacphlip_command_line)
        print(result.stderr)
        return None


def lifestyle_calls(accessions, filename = 'lifestyle_phages.fasta'):
    command = bacphlip_command()
    if not command:
        return None

    output_file = run_bacphlip(lifestyle_genomes(accessions, filename), command)
    if not output_file:
        return None

    table = pd.read_csv(output_file, sep = '\t', index_col = 0)
    calls = {str(accn).split()[0]:(row['Virulent'], row['Temperate'],
             'lytic' if row['Virulent'] >= row['Temperate'] else 'temperate')
             for accn, row in table.iterrows()}

    lytic = [accn for accn, call in calls.items() if call[2] == 'lytic']
    print(f'> {len(lytic)} lytic, {len(calls) - len(lytic)} temperate')

    return calls


def pool_accessions(similar_phages):

    return list(dict.fromkeys(accn for accns in similar_phages.values() for accn in accns))


def filter_temperate(similar_phages, calls):
    lytic_phages = {}
    dropped = set()

    for bact, accns in similar_phages.items():
        # phages without a call are kept, as BACPHLIP made no prediction for them
        keep = [accn for accn in accns if accn not in calls or calls[accn][2] != 'temperate']
        dropped.update(set(accns) - set(keep))
        if keep:
            lytic_phages[bact] = keep
        else:
            print(f'> No lytic candidates for {bact}, species excluded')

    print(f'> Excluded {len(dropped)} temperate phage(s) from the pool')

    return lytic_phages
