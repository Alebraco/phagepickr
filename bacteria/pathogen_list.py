import pandas as pd

def retrieve_pathogenic_list(): 
    #Download pathogenic bacteria list from Barlett et al.
    #Store it in a dataframe
    url = 'https://github.com/padpadpadpad/bartlett_et_al_2022_human_pathogens/raw/master/data/bacteria_human_pathogens.xlsx'
    bdf = pd.read_excel(url, sheet_name='Tab 6 Full List', usecols="F:G", skiprows=0)
    
    #Convert dataframe to list
    #Combine the genus and species column
    pblist = list(bdf['genus'] + ' ' + bdf['species'])
    
    #Removing random characters
    clean_patlist = [species.replace('¬†','') for species in pblist]
    return clean_patlist