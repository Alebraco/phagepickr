from Bio import Entrez,SeqIO
import time

def fetch_sequences(acclist):
  """Fetch amino acid sequences for given accession numbers.

  Args:
    acc (list): A list of accession numbers.

  Returns:
    list: The list of amino acid sequences.
  """

  aaseqs = [] # Initialize amino acid sequences list
  max_attempts = 15 # Set maximum number of attempts to avoid infinite loop.
  placeholder = "No Sequence Found" # Placeholder for missing sequences.
    
  # Iterate over each accession in the list.
  for accession in acclist: 
    attempt = 0 # Attempt counter
    sequence_fetched = False # Indicate successful retrieval.

    while attempt < max_attempts and sequence_fetched == False:
      try:
        # Fetch sequence from the protein database
        handle = Entrez.efetch(db = 'protein', id = accession, rettype = 'gb', retmode = 'text')
        output = SeqIO.parse(handle, 'gb')
        record = next(output, None)
        
        if record: 
          # If a sequence is found, append it to the list.
          aaseqs.append(str(record.seq))
          sequence_fetched = True
            
        else:
          # If sequence is missing, append placeholder text.
          print('No sequence found for accession number ', accession)
          aaseqs.append(placeholder)
        # Exit the loop after sequence has been processed.
        break

      except Exception as error:
        # Handle errors and network issues and retry after some time.
        sleeptime = 2 ** attempt
        print('Error fetching data, trying again in', sleeptime, 'seconds:', error)
        time.sleep(sleeptime) 
        attempt += 1
      
      finally:
        # Ensure handle is closed
        handle.close()

    # If retrieval is unsuccessful after all attempts, append placeholder
    if not sequence_fetched:
      print('Failed to retrieve data for accession number ', accession)
      aaseqs.append(placeholder) 

  return aaseqs
