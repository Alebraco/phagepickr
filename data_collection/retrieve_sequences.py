
from Bio import Entrez,SeqIO
import time

def fetch_sequences(acc):
  success = False
  sleep_time = 1

  try:
    handle = Entrez.efetch(db = 'protein', id = acc, rettype = 'gb', retmode = 'text')
    output = list(SeqIO.parse(handle, 'gb'))
    handle.close()
    sleep_time = 1

  except Exception as error:
    print('Error fetching data, trying again in', sleep_time,'seconds:', error)
    time.sleep(sleep_time)
    sleep_time *= 2

  #Reading sequences and adding them to a list
  aaseqs = [str(entry.seq) for entry in output]
  return aaseqs
