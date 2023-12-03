from .retrieve_ids import retrieve_ids
from .retrieve_titles import retrieve_summary, fix_unnamed
from .retrieve_sequences import fetch_sequences

#Retrieve receptor titles and sequences for a specific pathogenic host

def receptors(maxm,db,query):

  ids = retrieve_ids(maxm,db,query)
  titles, acc = retrieve_summary(ids,maxm)
  aaseqs = fetch_sequences(acc)
  titles = fix_unnamed(titles)

  return titles, aaseqs





