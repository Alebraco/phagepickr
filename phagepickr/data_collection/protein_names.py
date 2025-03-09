from Bio import Entrez
import time

def retrieve_titles(ids, db = 'ipg', maxrec = 50):
  """Retrieve protein names and accession numbers for given IDs from 'Identical 
    Protein Groups' NCBI database.

  Args:
    ids (list): A list of protein IDs for which to retrieve the name
    maxrec (int, optional): The number of records to retrieve for each batch
    db (str, optional): Database from which records are retrieved. 

  Returns:
    tuple: A tuple containing two lists. The first list contains the protein titles
      for each ID in the given list. The second list contains the accession numbers
      for each ID.
  """
  
  titles = [] # Initialize titles list
  start = 0 # Start index for batch retrieval
  sleep_time = 1 # Initial sleep time for retrying after an error

  while start < len(ids):
    idsfrag = ids[start:start + maxrec] # Get a fragment of IDs for a batch
    retrieval = False # Indicates successful retrieval

    while not retrieval:
      try:
        # Retrieve batch of summaries from the database
        handle = Entrez.esummary(db = db, id = idsfrag, retmax = maxrec)
        ipgsum = Entrez.read(handle)
        handle.close()
        retrieval = True
        sleep_time = 1 # Reset sleep time after successful request

      except Exception as error:
        print('Error retrieving data, trying again in', sleep_time,'seconds:', error)
        time.sleep(sleep_time)
        sleep_time *= 2

    # Extract titles and accession numbers from retrieved data
    for entry in ipgsum['DocumentSummarySet']['DocumentSummary']:
      titles.append(entry['Title'])

    start += maxrec # Update start index for next batch
    
  return titles


def fix_unnamed(titles):
  """Replace empty strings ('') with a placeholder ('unnamed protein v#'). 
    Modifies the list in place.

  Args:
    titles (list): A list of protein titles

  Returns:
    list: Updated list of protein titles
  """
  
  unnamed_count = 1 # Counter for unnamed proteins
  for index, title in enumerate(titles):
    if title == '':
      titles[index] = 'unnamed protein v' + str(unnamed_count)
      unnamed_count += 1
  return titles