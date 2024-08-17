from Bio import Entrez

def entrez_email():
  '''Prompt the user for an email address used for identification purposes.
  
  If repeated requests that violate NCBI policies are made, the user will be
  contacted by NCBI through this email before blocking access to the servers.
  
  '''
  print("Please enter your email address for NCBI Entrez.") 
  print("This is required for identification purposes by NCBI.")
  user_email = input("Enter your Entrez email: ")
  Entrez.email = user_email

def alignment_choice():
    valid = False
    while not valid:
        choice = int(input('How would you like to select phages?\n'
                       '1. Choose phages randomly\n'
                       '2. Align phage genomes for maximum diversity\n'
                       'Enter your choice (1 or 2): '))
        if choice == 1 or choice == 2:
            valid = True
        else: 
            print('Invalid choice. Please try again.')
    return int(choice)
