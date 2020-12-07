def read_elements(filename):
    """Return a list of lists with info about chem. elements read from the given file
    :param filename: string, path to a file with the elements database
    :return: list of tuples, each tuple containing name (string), number (int),
    and weight (float) for each element.
    """ 
    list=[]
    with open(filename) as f:
        for line in f:
            tup=(line.split()[0],int(line.split()[1]),float(line.split()[2]))
            list.append(tup)
        return list
if __name__ == "__main__":
    print(read_elements('elements.txt'))