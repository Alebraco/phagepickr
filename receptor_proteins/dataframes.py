import pandas as pd

#Creating DataFrame of Version 1 dictionary

df = pd.DataFrame(titles_unique, columns=['Protein Name'])
df[strain] = df['Protein Name'].isin(titles)

#Creating DataFrame of Version 2 dictionary
#Compared dictionary values (accumulative) with AA sequence values (unique for each query)
#Returns True/False

df2 = pd.DataFrame(protein_dictionary_v2.items(), columns=['Protein Name','AAseq'])
df2[strain] = df2['AAseq'].isin(aaseqs)
df2.drop('AAseq', axis = 1, inplace = True)

