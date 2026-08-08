def print_phage_cocktail(product, phageinfo, target, calls = None, accessions = None):
    flag = False
    selected = set(accessions) if accessions else set()
    accns = {record['phage']:record['acc'] for record in phageinfo if record['acc'] in selected}

    for phage in product:
        is_known = False
        for record in phageinfo:
            if record['phage'] == phage and record['host']== target:
                is_known = True
                break
        name = f'{phage}*' if is_known else phage
        if is_known:
            flag = True

        if calls and accns.get(phage) in calls:
            virulent, temperate, call = calls[accns[phage]]
            print(f'{name} - {call} (virulent: {virulent:.3f}, temperate: {temperate:.3f})')
        else:
            print(name)

    if flag:
        print('Confirmed phages are marked with an asterisk (*)')
    if calls:
        print('Warning: Lifestyle predictions might be inaccurate.')
