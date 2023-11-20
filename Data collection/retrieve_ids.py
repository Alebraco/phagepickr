get_ipython().system('pip install bio')
from Bio import Entrez,SeqIO
from Bio.SeqFeature import SeqFeature, FeatureLocation
import pandas as pd
import numpy as np
import time

Entrez.email = 'alekey039@hotmail.com'

def retrieve_ids(max, db, query):
  ids = []
  start = 0
  sleep_time = 1

  while(True):
    try:
      handle = Entrez.esearch(db = db, retmax = max, retstart = start, term = query)
      rec = Entrez.read(handle)
      handle.close()
      sleep_time = 1

    except Exception as error:
      print('Search failed, trying again in', sleep_time,'seconds:', error)
      time.sleep(sleep_time)
      sleep_time *= 2
      continue

    if len(rec['IdList']) == 0:
      break

    start += max
    ids += rec['IdList']
  return ids
