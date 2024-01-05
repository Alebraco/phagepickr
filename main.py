from data_collection.pathogen_processing import read_pathogens, query_pathogens
from utils.user_interaction import entrez_email
from utils.data_management import store_data

if __name__ == '__main__':
  entrez_email()
  upat = read_pathogens('uniquepat.txt')
  output_file = 'receptor_data.json'
  data = query_pathogens(upat, 200, output_file)
  store_data(data, output_file)
  
