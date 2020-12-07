def remove_duplicates(items):
    u = []
    d = []
    for item in items:
        if items.count(item) != 1:
            if u.count(item) == 0:
                u.append(item)                          
            elif d.count(item) == 1 and u.count(item) == 1 and items.count(item) == 2:
                pass  
            else:
                d.append(item)           
        else:
            u.append(item)
    return u, d


if __name__ == "__main__":
    print(remove_duplicates(['h','e','l','l','l','l','o']))
