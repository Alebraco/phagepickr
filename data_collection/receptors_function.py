from .protein_ids import retrieve_ids
from .protein_names import retrieve_titles, fix_unnamed

def receptors(query, recs = 50):
    '''Retrieve receptor titles and sequences for a specific pathogenic host. Use
    previously defined functions.
    
    Args:
      query (str): A string used to query the database. The format should match 
        the specific requirements of the database.
      maxrec (int, optional): The number of records to retrieve for each batch.
      
    Returns:
      tuple: A tuple containing two lists. The first list contains the protein 
        titles. The second list contains the corresponding amino acid sequences.
    
    '''
    ids = retrieve_ids(query, db = 'ipg', maxrec = recs)
    titles = retrieve_titles(ids, db = 'ipg', maxrec = recs)
    titles = fix_unnamed(titles)
    
    return titles






