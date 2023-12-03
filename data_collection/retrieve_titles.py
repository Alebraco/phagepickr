from Bio import Entrez,SeqIO
import time

#Retrieve titles and accessions

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
        ipgsum = Entrez.read(handle)
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

#Naming unnamed proteins

def fix_unnamed(titles):
  c = 1
  for i in range(len(titles)):
    if titles[i] == '':
      titles[i] = 'unnamed protein v'+str(c)
      c += 1
  return titles
