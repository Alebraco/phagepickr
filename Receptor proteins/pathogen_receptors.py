get_ipython().system('pip install bio')
from Bio import Entrez,SeqIO
from Bio.SeqFeature import SeqFeature, FeatureLocation
import pandas as pd
import numpy as np
import time

Entrez.email = 'alekey039@hotmail.com'

for pathogen in uniquepat:
    if 'Escherichia' in pathogen:
        query = str(pathogen)+'[ORGN] AND phage receptor[All fields]'
    else:
        query = str(pathogen)+'[ORGN] AND receptor[All fields]'
    titles, aaseqs = receptors(maxm,db,query)
    alltitles += titles
    allseqs += aaseqs
    species += pathogen

titles_unique = protdict(alltitles)
protein_dictionary_v2 = protdictv2(alltitles, allseqs)
