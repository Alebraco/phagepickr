def select_hosts(phinfo, patlist):
   pathost = []
   patstring = ' '.join(patlist)

   for phage in phinfo:
     if phage['host'] in patstring:
       pathost.append(phage)

   return pathost
