from Bio import Entrez
import time

def retrieve_ids(query, db, maxrec = 50):
  """Fetch IDs from an NCBI database.

  Args:
    maxrec (int, optional): The number of records to retrieve for each batch
    db (str): Database from which records are retrieved
    query (str): A string used to query the database. The format
      should match the specific requirements of the database.

  Returns:
    list: A list of IDs retrieved
  """
  
  ids = [] # Initialize IDs list
  start = 0 # Start index for batch retrieval
  sleep_time = 1 # Initial sleep time for retrying after an error

  while(True):
    try:
      # Requesting batch of IDs from the database
      handle = Entrez.esearch(db = db, retmax = maxrec, retstart = start, term = query)
      rec = Entrez.read(handle)
      handle.close()
      sleep_time = 1 # Reset sleep time after successful request

    except Exception as error:
      # Retry mechanism in case of error
      print('Search failed, trying again in', sleep_time,'seconds:', error)
      time.sleep(sleep_time)
      sleep_time *= 2
      continue

    # Break the loop if no more IDs are found
    if len(rec['IdList']) == 0:
      break

    # Update start index for next batch and extend IDs list
    start += maxrec
    ids += rec['IdList']
    
  return ids