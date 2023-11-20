get_ipython().system('pip install bio')
from Bio import Entrez,SeqIO
from Bio.SeqFeature import SeqFeature, FeatureLocation
import pandas as pd
import numpy as np
import time

def select_hosts(phinfo, patlist):
   pathost = []
   patstring = ' '.join(patlist)

   for phage in phinfo:
     if phage['host'] in patstring:
       pathost.append(phage)

   return pathost
