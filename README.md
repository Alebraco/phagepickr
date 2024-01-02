# phagetool
**An evolution-proof tool that identifies phage cocktails to treat bacterial infections**

The code is divided into two main parts: Data Collection and Bacteria.

### 1. Data Collection
This part of the code involves defining functions to fetch data from the NCBI database. It includes:

- **Function Definitions**:
    - `retrieve_ids`: Fetches IDs from an NCBI database.
    - `retrieve_titles`: Retrieves titles for given IDs from the 'Identical Protein Groups' NCBI database.
    - `fix_unnamed`: Renames unnamed proteins (empty strings) to maintain clarity in data.
    - `fetch_sequences`: Fetches amino acid sequences for given accession numbers.
    - `protdict` and `protdictv2`: Create dictionaries for protein data, based on unique titles or amino acid sequences
    - `receptors`: Combines previously defined functions (`retrieve_ids`, `retrieve_summary`, `fetch_sequences`, `fix_unnamed`) and returns a list of titles and sequences for a specific pathogen.

### 2. Pathogenic Bacteria
This section is focused on processing information related to pathogenic bacteria. It includes:

- **Downloading Pathogenic Bacteria List**: Fetching a list of pathogenic bacteria from Barlett et al. (2022).
  
- **Clean and Prepare Bacteria List**: Removing unwanted characters from the bacteria list and combining genus and species names.

- **Phage Hosts Data Collection**: `phageid_to_host` fetches information about phages, including their IDs and host.

- **Pathogenic Hosts Selection**: `select_hosts` compares phage hosts to the pathogenic bacteria list and keeps the information of phages with pathogenic hosts.
  

This script is a tool for extracting, processing, and organizing biological data from the NCBI database, focusing on pathogenic bacteria and their associated protein receptors. It utilizes the Entrez programming utilities from BioPython and employs various Python libraries for data handling and processing.
