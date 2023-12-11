#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install bio')
from Bio import Entrez,SeqIO
from Bio.SeqFeature import SeqFeature, FeatureLocation
import pandas as pd
import numpy as np
import time


# In[2]:


Entrez.email = 'alekey039@hotmail.com'


# In[3]:


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


# In[4]:


#Can be a separate function

max = 40
strain = 'Escherichia coli K-12'
db = 'ipg'
query = str(strain)+'[ORGN] AND receptor[All fields]'
#Execute the function with these parameters

ids = retrieve_ids(max, db, query)


# In[5]:


def retrieve_summary(ids, max):
  titles = []
  acc = []
  start = 0
  sleep_time = 1

  while start < len(ids):
    idsfrag = ids[start:start + max]
    retrieval = False

    while not retrieval:
      try:
        handle = Entrez.esummary(db='ipg', id = idsfrag, retmax = max)
        ipgsum = Entrez.read(handle, validate = False)
        handle.close()
        retrieval = True
        sleep_time = 1

      except Exception as error:
        print('Error retrieving data, trying again in', sleep_time,'seconds:', error)
        time.sleep(sleep_time)
        sleep_time *= 2

    for entry in ipgsum['DocumentSummarySet']['DocumentSummary']:
      titles.append(entry['Title'])
      acc.append(entry['Accession'])


    start += max
  return titles, acc


# In[6]:


max = 40
dbs = 'ipg'
#Execute the function with these parameters
titles, acc = retrieve_summary(ids, max)


# In[7]:


#Retrieving AA sequences

def fetch_sequences(acc):
    sleep_time = 1
    aaseqs = []

    for a in acc:
      try:
        handle = Entrez.efetch(db = 'protein', id = a, rettype = 'gb', retmode = 'text')
        #output = list(SeqIO.parse(handle, 'gb'))
        output = list(SeqIO.parse(handle, 'gb'))
        handle.close()
        if not output: 
            print('Sequence not found. Accession number:', a)
        for record in output:
            aaseqs.append(str(record.seq))

      except Exception as error:
        print('Error fetching data, trying again in', sleep_time,'seconds:', error)
        time.sleep(sleep_time)
        sleep_time *= 2

    #Reading sequences and adding them to a list
    #aaseqs = [str(entry.seq) for entry in output]
    return aaseqs


# In[8]:


#Execute the function above
aaseqs = fetch_sequences(acc)


# In[9]:


#Naming unnamed proteins
def fix_unnamed(titles):
  c = 1
  for i in range(len(titles)):
    if titles[i] == '':
      titles[i] = 'unnamed protein v'+str(c)
      c += 1
  return titles


# In[10]:


titles = fix_unnamed(titles)


# In[11]:


#Version 1
#Create a unique title list
#Aminoacid sequence not considered
#Comparison will be by protein name

def protdict (titles):
  titles_unique = []
  for title in titles:
    if title not in titles_unique:
      titles_unique.append(title)

  return titles_unique


# In[12]:


#Version 2 dictionary
#Create an alternative list that accounts for same protein names
#Unique keys, unique values
#Comparison will be by AA seq

def protdictv2 (titles, aaseqs):
  titles_version = []
  key_counter = {}
  protein_dictionary_v2 = {}

  for key in titles:
    if key in key_counter.keys():
      key_counter[key] += 1
      key_title = str(key) + ' v' + str(key_counter[key])
    else:
      key_counter[key] = 1
      key_title = key
    titles_version.append(key_title)

  for key, value in zip(titles_version, aaseqs):
    protein_dictionary_v2[key] = value

  return protein_dictionary_v2


# In[13]:


titles_unique = protdict(titles)
protein_dictionary_v2 = protdictv2(titles, aaseqs)


# In[14]:


#Creating DataFrame of Version 1 dictionary

df = pd.DataFrame(titles_unique, columns=['Protein Name'])
df[strain] = df['Protein Name'].isin(titles)

df


# In[15]:


#Creating DataFrame of Version 2 dictionary
#Compared dictionary values (accumulative) with AA sequence values (unique for each query)
#Returns True/False

df2 = pd.DataFrame(protein_dictionary_v2.items(), columns=['Protein Name','AAseq'])
df2[strain] = df2['AAseq'].isin(aaseqs)
df2.drop('AAseq', axis = 1, inplace = True)

df2


# In[16]:


#Download pathogenic bacteria list from Barlett et al.
#Store it in a dataframe
url = 'https://github.com/padpadpadpad/bartlett_et_al_2022_human_pathogens/raw/master/data/bacteria_human_pathogens.xlsx'
bdf = pd.read_excel(url, sheet_name='Tab 6 Full List', usecols="F:G", skiprows=0)


# In[17]:


#Convert dataframe to list
#Join the genus and species column

pblist = list(bdf['genus'] + ' ' + bdf['species'])


# In[18]:


# Found random characters
# Used .replace to remove them

clean_pathogen_list = [species.replace('¬†','') for species in pblist]


# In[19]:


max = 100
db = 'nucleotide'
query = 'Viruses[ORGN] AND phage[All fields] AND srcdb_refseq[PROP] \
NOT wgs[PROP] NOT cellular organisms[ORGN] NOT AC_000001:AC_999999[PACC]'

#Execute the function with these parameters
phageids = retrieve_ids(max, db, query)


# In[20]:


#Input: IDs of phages
#Output: List of bacterial hosts
#seq_start and seq_stop parameters retrieve the first feature only (source)
#In the source feature, there is information about the host

def phageid_to_host(phageids):
  phageinfo = []
  sleep_time = 1

  for id in phageids:
    phage_dict = {}
    try:
      handle = Entrez.efetch(db="nucleotide", id=id, rettype="gb",
                            retmode="text", seq_start = 1, seq_stop = 1)
      source = SeqIO.read(handle, 'gb')
      handle.close()

      features = source.features[0]
      qual = features.qualifiers

      strain = qual.get('host', qual.get('lab_host', None))

      if strain != None:
        strain = strain[0]
        phage_dict['phage'] = qual['organism'][0]
        phage_dict['id'] = id
        phage_dict['strain'] = strain

        split = strain.split(" ", 2)

        if len(split) > 1 and ("sp." in split[1] or "spp." in split[1]):
          species = split[0]
        elif len(split) > 1:
          species = split[0] + " " + split[1]
        else:
          species = split[0]
        phage_dict['host'] = species

        phageinfo.append(phage_dict)

      sleep_time = 1

    except Exception as error:
      print('Error fetching data, trying again in', sleep_time,'seconds:', error)
      time.sleep(sleep_time)
      sleep_time *= 2
      continue

  return phageinfo


# In[21]:


#phageinfo = phageid_to_host(phageids)


# In[22]:


# def select_hosts(phinfo, patlist):
#   pathost = []
#   patstring = ' '.join(patlist)

#   for phage in phinfo:
#     if phage['host'] in patstring:
#       pathost.append(phage)

#   return pathost


# In[23]:


#Create list of dictionaries for phages with pathogen hosts
# pathost = select_hosts(phageinfo, clean_pathogen_list)


# In[24]:


#List of unique pathogen hosts

# uniquepat = []
# for phage in pathost:
#   if phage['host'] not in uniquepat and phage['host'] not 'bacterium':
#     uniquepat.append(phage['host'])


# In[25]:


file_path = 'uniquepat.txt'

# Create an empty list to store the lines
upat = []

# Open the file and read each line
with open(file_path, 'r') as file:
    for line in file:
        # Strip newline characters and add to the list
        upat.append(line.strip())

# Print the list to verify the contents
print(upat)


# In[26]:


def receptors(maxm,db,query):

  ids = retrieve_ids(maxm,db,query)
  titles, acc = retrieve_summary(ids,maxm)
  aaseqs = fetch_sequences(acc)
  titles = fix_unnamed(titles)

  return titles, aaseqs


# In[28]:


maxm = 200
db = 'ipg'
alltitles = []
allseqs = []
species = [] 

for pathogen in upat:
    query = str(pathogen)+'[ORGN] AND receptor[All fields]'
    print(pathogen)
    titles, aaseqs = receptors(maxm,db,query)
    alltitles += titles
    allseqs += aaseqs
    species.extend([str(pathogen)]*len(titles))
    print(len(titles), len(aaseqs))
    

  #add species list (to link it to the phage)
  #run this locally



# In[ ]:


titles_unique = protdict(alltitles)
protein_dictionary_v2 = protdictv2(alltitles, allseqs)


# In[ ]:





# In[ ]:




