#!/usr/bin/env python -u
# -*- coding: utf-8 -*-

import argparse
from glob import glob
from phagepickr.utils.user_interaction import entrez_email, api_key
from phagepickr.utils.data_management import read_data
from phagepickr.cocktail.dataframe import receptor_df, produce_array, remove_ifmember
from phagepickr.cocktail.neighbors import nearest_bacteria, nearest_names, nearest_phages
from phagepickr.cocktail.random import random_cocktail
from phagepickr.cocktail.alignment import most_diverse_phages
from phagepickr.cocktail.phage_seqs import phage_genomes
from phagepickr.cocktail.final import indices_to_accn, accession_cocktail, final_cocktail
from phagepickr.utils.output import print_phage_cocktail

def cli():
    parser = argparse.ArgumentParser(description="PhagePickr: Design of evolution-proof bacteriophage cocktails", formatter_class=argparse.RawTextHelpFormatter)
    
    required = parser.add_argument_group('required arguments')
    required.add_argument("--target", "-t", metavar="<SPECIES>", required=True, help="Name of the target species (e.g., \"Escherichia coli\")")
    required.add_argument("--email", "-e", metavar="<EMAIL>", required=True, help="Your email (required for NCBI Entrez)")

    optional = parser.add_argument_group('optional arguments')
    optional.add_argument("--strategy", "-s", choices=["diverse", "random"], default="diverse",
                        help="Choose 'diverse' for maximum diversity or 'random' for random selection of phages (default=diverse)")
    optional.add_argument("--neighbors", metavar="n", type=int, default=3, help="Number of nearest neighbors to consider (default=3)")
    optional.add_argument("--k_value", metavar="k", type=int, default=1, help="Number of phage pairs that maximize genetic diversity (default=1)")
    optional.add_argument("--explore_only", "-i", action='store_true', help="Exclude known infecting phages in the selection (potential infectors only).")
    optional.add_argument("--api_key", metavar="<KEY>", help="NCBI API key")

    args = parser.parse_args()

    target = args.target
    print(f'Target species: {target}')
    choice = args.strategy
    entrez_email(args.entrez_email)
    explore = args.explore_only
    if explore:
        print('Including known infecting phages in the selection.')
    neighbors = args.neighbors

    if args.api_key:
        key = args.api_key
        api_key(key)
        print(f'Using NCBI API key: {key}')

    receptor_data = read_data('receptor_data.json')
    phageinfo = read_data('phagedicts.json')
    df = receptor_df(receptor_data)
    
    target_features = produce_array(target, df)
    target_features, features_data = remove_ifmember(target_features, target, df, explore)
    _, indices = nearest_bacteria(target_features, features_data, neighbors)
    similar = nearest_names(indices, df)
    similar_phages = nearest_phages(similar, phageinfo)
    
    if choice == "random":
        random_accs = random_cocktail(similar_phages)
        product = final_cocktail(random_accs, phageinfo)
        
    elif choice == "diverse":
        k_value = args.k_value if args.k_value else 1
        filename_ls = phage_genomes(similar_phages)
        distances_list, matrix_list, names_list = most_diverse_phages(filename_ls, k_value)
        diverse_accn = indices_to_accn(distances_list, matrix_list, names_list)
        candidate_accs = accession_cocktail(diverse_accn, similar_phages)
        product = final_cocktail(candidate_accs, phageinfo)

    print('Final Phage Cocktail:')
    print_phage_cocktail(product, phageinfo, target)

    for fasta_file in glob('*.fasta'):
        os.remove(fasta_file)

if __name__ == '__main__':
    cli()
