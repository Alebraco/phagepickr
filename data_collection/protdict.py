#Version 1
#Create a unique title list
#Aminoacid sequences not considered
#Comparison will be by protein name

def protdict (titles):
  titles_unique = []
  for title in titles:
    if title not in titles_unique:
      titles_unique.append(title)

  return titles_unique

#Version 2 dictionary
#Create an alternative list that accounts for same protein names
#Unique keys, unique values
#Comparison will be by AA seq

def protdictv2 (titles, aaseqs):
  titles_version = []
  key_counter = {}
  protein_dictionary_v2 = {}

  for key in titles:
    if key in key_counter.keys():
      key_counter[key] += 1
      key_title = str(key) + ' v' + str(key_counter[key])
    else:
      key_counter[key] = 1
      key_title = key
    titles_version.append(key_title)

  for key, value in zip(titles_version, aaseqs):
    protein_dictionary_v2[key] = value

  return protein_dictionary_v2
