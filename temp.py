# -*- coding: utf-8 -*-

receptor_dict = read_data('receptor_data.json')
        
unique_sp = receptor_dict.keys()
unique_titles = sorted(set(receptor_dict.values()))
######

df = pd.DataFrame(index = unique_sp, columns = unique_titles)
for sp in df.index:
    df.loc[sp] = df.columns.isin(receptor_dict.get(sp, False)).astype(int)
####
features_array = df.to_numpy()

if target in the list: remove it and compare it with the other species
else: run receptors function on target, and then compare it.

if target in unique_sp:
    test = unique_sp[174] #the name of the target
    test_features = features_array[[174]] # the list of 1s and 0s

modified_array = np.delete(features_array, 174, axis=0)
modified_labels = list(unique_sp)
modified_labels.pop(174)

nn_model = NearestNeighbors(n_neighbors = 5, metric = 'hamming')
nn_model.fit(modified_array)

distances, indices = nn_model.kneighbors(test_features, n_neighbors = 5)


similar = []
for i in indices[0]:
    print(modified_labels[i])
    similar.append(modified_labels[i])
    
with open('phagedicts.json', 'r') as f:
    phageinfo = json.load(f)
    
cocktail = {host:[record['id'] for record in phageinfo if 
                  record['host'] == host] for host in similar}

seqs = []
for bact, ids in cocktail.items():
    handle = Entrez.efetch(db='nucleotide', id = ids, rettype = 'fasta', retmode = 'text')
    for record in SeqIO.parse(handle, 'fasta'):
        seqs.append(record)
    handle.close()
    
with open('phages.fasta', 'w') as file:
    SeqIO.write(seqs, file, 'fasta')
    
def align_sequences(input_file, output_file):
    mafft_command = f'mafft --auto {input_file} > {output_file}'
    subprocess.call(mafft_command, shell=True)



