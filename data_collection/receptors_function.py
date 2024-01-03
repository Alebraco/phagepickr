from .protein_ids import retrieve_ids
from .protein_names import retrieve_titles, fix_unnamed
from .sequences import fetch_sequences

def receptors(query, maxrec = 50):
  '''Retrieve receptor titles and sequences for a specific pathogenic host. Use
  previously defined functions.
  
  Args:
    query (str): A string used to query the database. The format should match 
      the specific requirements of the database.
    maxrec (int, optional): The number of records to retrieve for each batch
    
  Returns:
    tuple: A tuple containing two lists. The first list contains the protein 
      titles. The second list contains the corresponding amino acid sequences.
  
  '''

  ids = retrieve_ids(query, db = 'ipg', maxrec = maxrec)
  titles, acc = retrieve_titles(ids, db = 'ipg', maxrec = maxrec)
  aaseqs = fetch_sequences(acc)
  titles = fix_unnamed(titles)

  return titles, aaseqs







