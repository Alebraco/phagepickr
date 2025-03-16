#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import subprocess
from Bio import AlignIO
from Bio.Phylo.TreeConstruction import DistanceCalculator
import heapq
import numpy as np
import platform



def align_sequences(input_file, output_file):
    print(f'Running alignment: {input_file}')
    
    if platform.system() == 'Windows':
       mafft_command = f'wsl.exe mafft --auto --quiet {input_file} > {output_file}' 
       result = subprocess.run(mafft_command, shell=True, capture_output = True)   
    else:
        mafft_command = f'mafft --auto --quiet {input_file} > {output_file}'
        
        result = subprocess.run(mafft_command, shell=True, capture_output = True)
        
    if result.returncode == 0:
        print('- Alignment performed successfully')
    else: 
        print('Error generating alignment')
        print(mafft_command)
        print(result.stderr)

def distance_matrix(input_file):
    calculator = DistanceCalculator('identity')
    alignment = AlignIO.read(input_file, 'fasta')
    names = [record.id for record in alignment]
    matrix = calculator.get_distance(alignment)
    
    return matrix, names 

def top_distances(matrix, k = 1):
    array = np.array(matrix)

    minheap = [] # Initialize heap structure

    for i in range(len(array)):
        for j in range(i):
            d = array[i,j] # Distance between two samples
            if len(minheap) < k: # If heap is less than k, add the element
                heapq.heappush(minheap, (d, i, j)) 
            elif d > minheap[0][0]: # If distance is greater than root
                # push new element and pop current
                heapq.heappushpop(minheap, (d, i, j))
    return minheap

def most_diverse_phages(filename_ls, k = 1): #time consuming, genome alignment
    sorted_distances_list = []
    phage_matrix_list = []
    phage_names_list = []
    
    for file in filename_ls:
        aligned_file = f'aligned{file}'
        align_sequences(file, aligned_file)
        matrix, names = distance_matrix(aligned_file)
        sorted_distances = top_distances(matrix, k)
        
        phage_matrix_list.append(matrix)
        phage_names_list.append(names)
        sorted_distances_list.append(sorted_distances)
        
    return sorted_distances_list, phage_matrix_list, phage_names_list