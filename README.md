# phagetool
**An evolution-proof tool that identifies phage cocktails to treat bacterial infections**

The code is divided into three main parts: Data Collection, Pathogenic Bacteria, and Protein Receptors. 

### 1. Data Collection
This part of the code involves defining functions to fetch data from the NCBI database. It includes:

- **Function Definitions**:
    - `retrieve_ids`: Fetches IDs from the 'Identical Protein Groups' NCBI database.
    - `retrieve_summary`: Retrieves titles for given IDs from the database.
    - `fetch_sequences`: Fetches amino acid sequences for given accession numbers.
    - `fix_unnamed`: Renames unnamed proteins to maintain clarity in data.
    - `protdict` and `protdictv2`: Create dictionaries for protein data, based on unique titles or amino acid sequences

### 2. Pathogenic Bacteria
This section is focused on processing information related to pathogenic bacteria. It includes:

- **Downloading Pathogenic Bacteria List**: Fetching a list of pathogenic bacteria from an Barlett et al.
  
- **Clean and Prepare Bacteria List**: Removing unwanted characters from the bacteria list and combining genus and species names.

- **Phage Hosts Data Collection**: `phageid_to_host` fetches information about phages, including their IDs and host.

- **Pathogenic Hosts Selection**: `select_hosts` compares phage hosts to the pathogenic bacteria list and keeps the information of phages with pathogenic hosts.

### 3. Protein Receptors
This part identifies protein receptors related to the pathogenic bacteria. It includes:

- **Receptor Data Collection**: The `receptors` function combines previously defined functions (`retrieve_ids`, `retrieve_summary`, `fetch_sequences`, `fix_unnamed`) to collect data about protein receptors related to each pathogen.

- **Processing Pathogens**: Uses the `receptors` function on the pathogenic hosts list to collect data about their protein receptors. 

- **Data Structuring**: Creates dictionaries of protein titles and sequences, structuring the data into dataframes for easier comparison.

This script is a tool for extracting, processing, and organizing biological data from the NCBI database, focusing on pathogenic bacteria and their associated protein receptors. It utilizes the Entrez programming utilities from BioPython and employs various Python libraries for data handling and processing.
