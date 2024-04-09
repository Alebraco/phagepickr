# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 16:54:07 2024

@author: aleke
"""

from data_collection.pathogen_processing import read_pathogens, query_pathogens
from utils.user_interaction import entrez_email
from utils.data_management import store_data

if __name__ == '__main__':
  entrez_email()
  upat = read_pathogens('uniquepat.txt')
  output_file = 'receptor_data.json'
  data = query_pathogens(upat, 200, output_file)
  store_data(data, output_file)
  
  target = input('Enter the species you would like a cocktail for: ')
  receptor_dict = read_data('receptor_data.json')
  unique_sp = sorted(set(receptor_dict.keys())) 
  unique_titles = sorted(set(receptor_dict.values()))
  
  df = pd.DataFrame(index = unique_sp, columns = unique_titles)
  for sp in df.index:
      df.loc[sp] = df.columns.isin(receptor_dict.get(sp, False)).astype(int)

  