from Bio import Entrez,SeqIO
from Bio.SeqFeature import SeqFeature, FeatureLocation
import time

#Use phage IDs to retrieve host and strain information
def phageid_to_host(phageids):
  phageinfo = []
  sleep_time = 1

  for id in phageids:
    phage_dict = {}
    try:
      handle = Entrez.efetch(db="nucleotide", id=id, rettype="gb",
                            retmode="text", seq_start = 1, seq_stop = 1)
      source = SeqIO.read(handle, 'gb')
      handle.close()

      features = source.features[0]
      qual = features.qualifiers

      strain = qual.get('host', qual.get('lab_host', None))

      if strain != None:
        strain = strain[0]
        phage_dict['phage'] = qual['organism'][0]
        phage_dict['id'] = id
        phage_dict['acc'] = source.id
        phage_dict['strain'] = strain

        split = strain.split(" ", 2)

        if len(split) > 1 and ("sp." in split[1] or "spp." in split[1]):
          species = split[0]
        elif len(split) > 1:
          species = split[0] + " " + split[1]
        else:
          species = split[0]
        phage_dict['host'] = species

        phageinfo.append(phage_dict)

      sleep_time = 1

    except Exception as error:
      print('Error fetching data, trying again in', sleep_time,'seconds:', error)
      time.sleep(sleep_time)
      sleep_time *= 2
      continue

  return phageinfo


