# -*- coding: utf-8 -*-


from utils.user_interaction import entrez_email, alignment_choice
from utils.data_management import read_data
from cocktail.dataframe import receptor_df, produce_array, remove_ifmember
from cocktail.neighbors import nearest_bacteria, nearest_names, nearest_phages
from cocktail.random import random_cocktail
from cocktail.alignment import most_diverse_phages
from cocktail.phage_seqs import phage_genomes
from cocktail.final import indices_to_accn, accession_cocktail, final_cocktail

if __name__ == '__main__':
    entrez_email()
    receptor_data = read_data('receptor_data.json')
    phageinfo = read_data('phagedicts.json')
    
    df = receptor_df(receptor_data)
    target = input('Enter the target species:')

    target_features = produce_array(target, df)
    target_features, features_data = remove_ifmember(target_features, target, df)
    distances, indices = nearest_bacteria(target_features, features_data, neighbors = 3)
    similar = nearest_names(indices, df)
    similar_phages = nearest_phages(similar, phageinfo)
    
    choice = alignment_choice()
    
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