from Bio import Entrez
import sys

def entrez_email(user_email):
  '''Prompt the user for an email address used for identification purposes.
  
  If repeated requests that violate NCBI policies are made, the user will be
  contacted by NCBI through this email before blocking access to the servers.
  
  '''
  print(f'Using provided Entrez email: {user_email}')
  Entrez.email = user_email

def alignment_choice(choice):
    '''Prompt the user to choose between random and aligned phage selection.'''
    if choice not in ["1", "2"]:
        print('Invalid choice. Please enter 1 (random selection) or 2 (align for maximum diversity).')
        sys.exit(1)
    if choice == "1":
        print('Using random selection.')
    else:
        print('Using aligned selection.')
    return int(choice)

def api_key(key):
    '''Let user provide their NCBI API key.'''
    Entrez.api_key = key
    print(f'Using provided API key: {key}')
