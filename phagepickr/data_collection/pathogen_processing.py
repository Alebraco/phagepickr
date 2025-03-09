from phagepickr.utils.data_management import read_data, store_data
from phagepickr.data_collection.receptors_function import receptors

def read_pathogens(file):
  '''Create a list of unique pathogenic species from a text file.
  Each line must contain an individual pathogen name.
  
  Args:
    file (str): File path of the text file with the pathogen names.
  Returns:
    list: A list of unique pathogenic species.
  '''
  # Open the file and read each line
  with open(file, 'r') as f: 
    upat = [line.strip() for line in f]
  return upat


def query_pathogens(upat, maxrec, output_file):
  '''Query information about receptor proteins for each pathogen
  and save the data in a dictionary.
  
  Args:
    upat (str): List of pathogenic species to query
    maxrec (int): Maximum number of records to retrieve for each batch.
    output_file (str, optional): File path where the data will be saved
  Returns:
    dict: A dictionary of the collected data with 3 keys (titles, sequences,
     and species).
  '''
  
  # Initialize a data dictionary to store the results
  data = {'titles': [], 'sequences': [], 'species': []}
  
  # Read existing data from the output file, if any
  # Useful in case of interruption
  saved_data = read_data(output_file)
  # Initialize a counter to save batches
  element_counter = 0

  # If data already exists, store it in the dictionary
  if saved_data != None:
    data = saved_data
  # Keep track of already processed pathogens, if any
  processed_pathogens = set(data['species'])
  

  # Iterate over each pathogen and query for receptor proteins
  for pathogen in upat:
    
    # Skip pathogen if already processed
    if pathogen in processed_pathogens:
      continue
    
    query = pathogen + '[ORGN] AND receptor[All fields]'
    # Retrieve protein names and sequences for current pathogen
    titles, aaseqs = receptors(query, maxrec)
    # Store the data in the dictionary
    data['titles'].extend(titles)
    data['sequences'].extend(aaseqs)
    data['species'].extend([pathogen]*len(titles))
    # Lists should be of the same length

    # Update the counter with the number of elements in each list
    element_counter += len(titles)
    # If 10 000 elements or more, store the data 
    if element_counter >= 10000:
        store_data(data, output_file)
        element_counter = 0 # Reset the counter after saving data
        
  # Return the dictionary with data on receptor proteins
  return data
