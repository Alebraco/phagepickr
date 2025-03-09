#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import random

def random_cocktail(similar_phages):
    random_accs = []
    phagelist = similar_phages.values()
    minrand = len(min(phagelist,key = len))
    valid = False
    while not valid:
        try:
            selection_str = input(f'Choose up to {minrand} phage(s) for each species: ')
            selection = int(selection_str)
            if selection <= minrand:
                valid = True
            else:
                print('Invalid choice. Please choose a valid number.')
        except ValueError:
            print('Invalid choice. Please enter an integer.')
            
    for phages in phagelist:
        random_phages = random.sample(phages, selection)
        random_accs.extend(random_phages)
        
    return random_accs
