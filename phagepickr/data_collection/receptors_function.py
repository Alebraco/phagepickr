from phagepickr.data_collection.protein_ids import retrieve_ids
from phagepickr.data_collection.protein_names import retrieve_titles, fix_unnamed

def receptors(query, recs=8000):
    """Retrieve receptor titles for a specific pathogenic host using
    previously defined functions.

    Args:
        query (str): A string used to query the database. The format should match 
            the specific requirements of the database.
        recs (int, optional): The number of records to retrieve for each batch.

    Returns:
        list: A list containing the protein titles.
    """
    try:
        print(f"Querying database with query: {query}")
        ids = retrieve_ids(query, db='ipg', maxrec=recs)
        print(f"Retrieved IDs")
        if not ids:
            print("No IDs retrieved.")
            return []

        print("Retrieving titles for the retrieved IDs.")
        titles = retrieve_titles(ids, db='ipg', maxrec=recs)
        print(f"Retrieved titles")
        if not titles:
            print("No titles retrieved.")
            return []

        print("Fixing unnamed titles.")
        titles = fix_unnamed(titles)
        print(f"Final titles obtained.")
        return titles

    except Exception as e:
        print(f"An error occurred: {e}")
        return []






