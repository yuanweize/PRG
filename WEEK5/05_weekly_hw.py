def combine_elements(el1, el2):
    list = []
    for b in el1:
        for x in el2:
            a = b+x
            list.append(a)
    return list