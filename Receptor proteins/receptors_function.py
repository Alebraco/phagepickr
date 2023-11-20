get_ipython().system('pip install bio')
from Bio import Entrez,SeqIO
from Bio.SeqFeature import SeqFeature, FeatureLocation
import pandas as pd
import numpy as np
import time

#Retrieve receptor titles and sequences for a specific pathogenic host

def receptors(maxm,db,query):

  ids = retrieve_ids(maxm,db,query)
  titles, acc = retrieve_summary(ids,maxm)
  aaseqs = fetch_sequences(acc)
  titles = fix_unnamed(titles)

  return titles, aaseqs





