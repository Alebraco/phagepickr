get_ipython().system('pip install bio')
from Bio import Entrez,SeqIO
from Bio.SeqFeature import SeqFeature, FeatureLocation
import pandas as pd
import numpy as np
import time

Entrez.email = 'alekey039@hotmail.com'

#Retrieve phage IDs with previously defined function
phageids = retrieve_ids(max, db, query)

#Retrieve host information using phage IDs
phageinfo = phageid_to_host(phageids)

#Create list of dictionaries for phages with pathogen hosts
pathost = select_hosts(phageinfo, clean_pathogen_list)

#Create list of unique pathogen hosts
uniquepat = []
for phage in pathost:
    if phage['host'] not in uniquepat:
        uniquepat.append(phage['host'])
