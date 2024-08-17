#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def indices_to_accn(sorted_distances_list, phage_matrix_list):
    diverse_accn = []
    for sorted_distances, phage_matrix in sorted_distances_list, phage_matrix_list:
        unique_indices = set()
        
        for _, i, j in sorted_distances: 
            unique_indices.update([i, j])
            
        diverse_accn.extend(phage_matrix.names[ind] for ind in unique_indices)
    return diverse_accn

def accession_cocktail(diverse_accn, similar_phages):
    candidate_accs = []
    accn_set = set(diverse_accn)
    
    for bact, accns in similar_phages.items(): 
        if len(accns) > 2:
            candidate_accs.extend([accn for accn in accns if accn in accn_set])
        else:
            candidate_accs.extend(accns)
    return candidate_accs

def final_cocktail(candidate_accs, phageinfo):
    
    return [rec['phage'] for rec in phageinfo if rec['acc'] in candidate_accs]
