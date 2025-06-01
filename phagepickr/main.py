#!/usr/bin/env python -u
# -*- coding: utf-8 -*-

import sys
from phagepickr.utils.user_interaction import entrez_email, alignment_choice, api_key
from phagepickr.utils.data_management import read_data
from phagepickr.cocktail.dataframe import receptor_df, produce_array, remove_ifmember
from phagepickr.cocktail.neighbors import nearest_bacteria, nearest_names, nearest_phages
from phagepickr.cocktail.random import random_cocktail
from phagepickr.cocktail.alignment import most_diverse_phages
from phagepickr.cocktail.phage_seqs import phage_genomes
from phagepickr.cocktail.final import indices_to_accn, accession_cocktail, final_cocktail
from phagepickr.utils.output import print_phage_cocktail

def cli():
    if len(sys.argv) != 5:
        print(
            "Usage: phagepickr <target_species> <alignment_choice> <entrez_email> <include_known>\n"
            "  <target_species>: Name of the species (use quotes: \"Escherichia coli\")\n"
            "  <alignment_choice>: 1 for diverse phages, 0 for random selection\n"
            "  <entrez_email>: Your email (required for NCBI Entrez)\n"
            "  <include_known>: 1 to include known infecting phages, 0 to exclude them\n"
        )
        sys.exit(1)
    
    target = sys.argv[1]
    print(f'Target species: {target}')
    choice = alignment_choice(sys.argv[2])
    entrez_email(sys.argv[3])
    include_known = int(sys.argv[4])
    api_key('c821b70c4172a5f198e7fcf93890df4a2d08')

    receptor_data = read_data('receptor_data.json')
    phageinfo = read_data('phagedicts.json')
    
    df = receptor_df(receptor_data)

    target_features = produce_array(target, df)
    target_features, features_data = remove_ifmember(target_features, target, df, include_known)
    _, indices = nearest_bacteria(target_features, features_data, neighbors = 3)
    similar = nearest_names(indices, df)
    similar_phages = nearest_phages(similar, phageinfo)
    
    if choice == 1:
        random_accs = random_cocktail(similar_phages)
        product = final_cocktail(random_accs, phageinfo)
        
    else:
        filename_ls = phage_genomes(similar_phages)
        distances_list, matrix_list, names_list = most_diverse_phages(filename_ls, k = 1)
        diverse_accn = indices_to_accn(distances_list, matrix_list, names_list)
        candidate_accs = accession_cocktail(diverse_accn, similar_phages)
        product = final_cocktail(candidate_accs, phageinfo)
        
    print('Final Phage Cocktail:')
    print_phage_cocktail(product, phageinfo, target)

if __name__ == '__main__':
    cli()
