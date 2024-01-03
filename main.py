from data_collection.receptors_function import receptors
from Bio import Entrez

print("Please enter your email address for NCBI Entrez. This is required for identification purposes by NCBI when making requests.")
user_email = input("Enter your Entrez email: ")
Entrez.email = user_email

file = 'uniquepat.txt'
with open(file, 'r') as f:
  upat = [line.strip() for line in f]
  

maxrec = 200
alltitles = []
allseqs = []
species = []

for pathogen in upat:
    query = str(pathogen)+'[ORGN] AND receptor[All fields]'
    print(pathogen)
    titles, aaseqs = receptors(query, maxrec)
    alltitles += titles
    allseqs += aaseqs
    species.extend([str(pathogen)]*len(titles))
    print(len(titles), len(aaseqs))




