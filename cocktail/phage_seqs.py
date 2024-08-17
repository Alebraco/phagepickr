#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from Bio import Entrez, SeqIO


def phage_genomes(similar_phages):
        
        filename_ls = []
        for bact, phages in similar_phages.items():
            if len(phages) > 2:
                filename = f'{"_".join(bact.split())}_phages.fasta'
                filename_ls.append(filename)
                seqs = []
                
                handle = Entrez.efetch(db='nucleotide', id = phages, rettype = 'fasta', retmode = 'text')
                for record in SeqIO.parse(handle, 'fasta'):
                    seqs.append(record)
                handle.close()
            
            with open(filename, 'w') as file: 
                SeqIO.write(seqs, file, 'fasta')
            
        return filename_ls