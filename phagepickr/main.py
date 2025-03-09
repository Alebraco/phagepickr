# -*- coding: utf-8 -*-

import sys
import os
import io
from phagepickr.utils.user_interaction import entrez_email, alignment_choice
from phagepickr.utils.data_management import read_data
from phagepickr.cocktail.dataframe import receptor_df, produce_array, remove_ifmember
from phagepickr.cocktail.neighbors import nearest_bacteria, nearest_names, nearest_phages
from phagepickr.cocktail.random import random_cocktail
from phagepickr.cocktail.alignment import most_diverse_phages
from phagepickr.cocktail.phage_seqs import phage_genomes
from phagepickr.cocktail.final import indices_to_accn, accession_cocktail, final_cocktail

if hasattr(sys.stdout, 'buffer'):
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, write_through=True)

def cli():
    if len(sys.argv) != 4:
        print('Usage: phagepickr <target_species> <alignment_choice> <entrez_email>')
        sys.exit(1)
    
    target = sys.argv[1]
    print(f'Target species: {target}')
    choice = alignment_choice(sys.argv[2])
    entrez_email(sys.argv[3])
   
    receptor_data = read_data('receptor_data.json')
    phageinfo = read_data('phagedicts.json')
    
    df = receptor_df(receptor_data)

    target_features = produce_array(target, df)
    target_features, features_data = remove_ifmember(target_features, target, df)
    _, indices = nearest_bacteria(target_features, features_data, neighbors = 3)
    similar = nearest_names(indices, df)
    similar_phages = nearest_phages(similar, phageinfo)
    
    if choice == 1:
        random_accs = random_cocktail(similar_phages)
        product = final_cocktail(random_accs, phageinfo)
        
    else:
        filename_ls = phage_genomes(similar_phages)
        phage_distances, phage_matrix = most_diverse_phages(filename_ls, k = 1)
        diverse_accn = indices_to_accn(phage_distances, phage_matrix)
        candidate_accs = accession_cocktail(diverse_accn, similar_phages)
        product = final_cocktail(candidate_accs, phageinfo)
        
    print(product)

if __name__ == '__main__':
    cli()