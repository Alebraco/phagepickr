from Bio import Entrez
import time

def retrieve_ids(query, db, maxrec=8000):
    """Fetch IDs from an NCBI database.

    Args:
        query (str): A string used to query the database.
        db (str): Database from which records are retrieved.
        maxrec (int, optional): The number of records to retrieve per batch.

    Returns:
        list: A list of IDs retrieved.
    """
    ids = []  # Initialize IDs list
    start = 0  # Start index for batch retrieval
    sleep_time = 1  # Initial sleep time for retrying after an error

    try:
        # Get the total number of records
        with Entrez.esearch(db=db, term=query, retmax=1) as handle:
            rec = Entrez.read(handle)
            total_records = int(rec.get("Count", 0))
    except Exception as error:
        print("Initial search failed:", error)
        return []

    while start < total_records:
        try:
            with Entrez.esearch(db=db, term=query, retmax=maxrec, retstart=start) as handle:
                rec = Entrez.read(handle)
            if not rec["IdList"]:  # Break the loop if no more IDs are found
                break

            ids.extend(rec["IdList"])
            start += maxrec
            sleep_time = 1

        except Exception as error:
            print(f"Search failed, retrying in {sleep_time} seconds:", error)
            time.sleep(sleep_time)
            sleep_time = min(sleep_time * 2, 60)
    return ids
