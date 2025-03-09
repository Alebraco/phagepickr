from phagepickr.bacteria.pathogen_list import retrieve_pathogenic_list
from phagepickr.bacteria.phage_host import phageid_to_host
from phagepickr.bacteria.select_hosts import select_hosts
from phagepickr.data_collection.protein_ids import retrieve_ids

clean_patlist = retrieve_pathogenic_list()

#Retrieve phage IDs with previously defined function
query = 'Viruses[ORGN] AND phage[All fields] AND srcdb_refseq[PROP] \
NOT wgs[PROP] NOT cellular organisms[ORGN] NOT AC_000001:AC_999999[PACC]'

phageids = retrieve_ids(query, db = 'nucleotide')

#Retrieve host information using phage IDs
phageinfo = phageid_to_host(phageids)

#Create list of dictionaries for phages with pathogen hosts
phagedict = select_hosts(phageinfo, clean_patlist)

#Create list of unique pathogen hosts
uniquepat = sorted(set(clean_patlist))
