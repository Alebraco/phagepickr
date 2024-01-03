# Version 1

def unique_titles (titles):
  '''Take a list of titles and create a new list of only unique titles. This 
    function does not consider aminoacid sequences. 
   
   Args:
        titles (list): A list of protein names.

    Returns:
        list: A list of unique protein names.
    '''
  
  return list(set(titles))

#Version 2 

def protdict (titles, aaseqs):
  '''Create a dictionary of protein names and amino acid sequences. Proteins 
  with the same name are labeled differently (v(n) suffix) to maintain uniqueness.
   
  Args:
    titles (list): A list of protein names.
    aaseqs (list): A list of corresponding amino acid sequences (lists must be
      the same length).

  Returns:
    dict: A dictionary of unique protein names (keys) and amino acid sequences
      (values).
  '''
  
  titles_version = [] # Initialize list of modified protein names.
  key_counter = {} # Initialize dict to monitor number of protein occurrences.
  protein_dictionary_v2 = {} # Initialize final protein dictionary.

  for title in titles:
    if title in key_counter:
      # If protein name already exists, increase the counter.
      key_counter[title] += 1
      # Append a modified protein name with a version number.
      key = str(title) + ' v' + str(key_counter[title])
    else:
      # If first occurrence, append protein name as is.
      key_counter[title] = 1
      key = title
    titles_version.append(key)

  # Populate protein dictionary with modified names and sequences
  for title, seq in zip(titles_version, aaseqs):
    protein_dictionary[title] = seq

  return protein_dictionary
