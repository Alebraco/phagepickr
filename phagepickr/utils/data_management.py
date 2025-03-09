import json

def read_data(file):
  '''
  Reads data from a JSON file.

  Args:
    file (str): The path of the file to be read
  Returns:
    dict or None: A dictionary with data read from
      the file or None if the file cannot be read.
  '''
  try:
    with open(file, 'r') as f:
        data = json.load(f)
    return data
  # Return None if the file cannot be read or does not exist 
  except:
    return None

def store_data(data, file):
  '''Saves data to a JSON file.
  Existing data in the file will be overwritten.
  
  Args:
    data (dict): The data to be saved.
    file (str): The path of the file where
      data will be saved.
  
  '''
  try:
    with open(file, 'w') as f:
        json.dump(data, f)
  except Exception as error:
    print('Error writing to file:', error)
    
      
