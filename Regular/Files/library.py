def load_library(filename):
    """
    :param filename: Path to a text file (with contents similar to those above) containing the individual books.
    :return dic: The function shall produce a dictionary where the book titles are used as keys and the authors' names are stored as values.
    """
    dic={}
    with open(filename) as f:
        #open file as f
        for line in f:
            #read line by line
            line=line.strip()
            #del \n
            key=line.split("|")[0]
            #split by '|' use frist word as key
            value=line.split("|")[1]
            #split by '|' use Second word as value
            dic[key]=value
            #Store key and value
        return dic


def index_by_author(dic):
    """
    :param dic: A dictionary with book titles as keys and book authors as values (the same structure as produced by load_library() function).
    :return dicc: A dictionary containing book authors as keys and a list of all books of the respective author as values.
    """
    dicc={}
    d=[]
    for value, key in dic.items():
        dicc[key]=value
        #Reverse key and value store to dicc
        d.append(dicc.copy())
        #store to list d
        dicc.clear()
        #clear dicc waiting for next item
    for i in d:
        for k,v in i.items():
            dicc.setdefault(k, []).append(v)
            #store authors as key, book name as value to a list which in dicc
    return dicc

def report_author_counts(lib_fpath, rep_filepath):
    """
    which shall compute the number of books of each author and the total number of books, and shall store this information in another text file.
    :param lib_fpath: Path to a library text file (containing records for individual books).
    :param rep_filepath: Path to report text file that shall be created by this function.
    """
    dic1=index_by_author(load_library(lib_fpath))
    #give me a dic, key is author value is a list of books name 
    file = open(rep_filepath,'w') 
    #prepare writing report file
    for k,v in dic1.items():
	    file.write(str(k)+': '+str(len(v))+'\n')
        #The key is the author name, and the length of the list is the number of books.
    count = 0
    for k, y in dic1.items():
        count+=len(y)
        #Total books sum
    file.write('TOTAL BOOKS: '+str(count))
    file.close()