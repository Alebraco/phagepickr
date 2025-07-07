def print_phage_cocktail(product, phageinfo, target):
    flag = False
    for phage in product:
        is_known = False
        for record in phageinfo:
            if record['phage'] == phage and record['host']== target:
                is_known = True
                break
        if is_known:
            print(f"{phage}*")
            flag = True
        else:
            print(phage)
    if flag:
        print('Confirmed phages are marked with an asterisk (*)')