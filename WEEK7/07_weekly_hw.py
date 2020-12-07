def combine_dict(d1, d2):
    for key,value in d2.items():
        if key in d1:
            d1[key]+=value
        else:
            d1[key]=value
    return d1

