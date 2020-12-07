from collections import Counter
def compute_word_importance(fpath1, fpath2):
    """
    word different
    :param fpath1: Path to the first text file.
    :param fpath2: Path to the second text file.
    :return: Counter object containing for each word the difference between counts of that word in the first and in the second file.
    """
    d1=[]
    d2=[]
    with open(fpath1) as f1, open(fpath2) as f2:
        for wd1 in f1.read().split():
            d1.append(wd1)
            #Split the word in a line of fpath1 to store the list d1
        for wd2 in f2.read().split():
            d2.append(wd2)
            #Split the word in a line of fpath2 to store the list d2
    cnt1=Counter(d1)
    #num of elements in d1
    cnt1.subtract(Counter(d2))
    #Compute the difference between d1 and d2 as cnt1
    return cnt1

if __name__ == "__main__":
    print(compute_word_importance('text1.txt', 'text2.txt'))
    # diy counter
    
    # d={}
    # d1={}
    # td={}
    # with open(fpath1, 'r') as f1:
    #     with open(fpath2, 'r') as f2:
    #         for wd1 in f1.read().split():
    #             if wd1 in d:
    #                 d[wd1]+=1
    #             else:
    #                 d[wd1]=1
    #         for wd2 in f2.read().split():
    #             if wd2 in d1:
    #                 d1[wd2]+=1
    #             else:
    #                 d1[wd2]=1
    # wds = set(d.keys()) | set(d1.keys())
    # # All word store to wds
    # for word in wds:
    #     if word in d and word in d1:
    # # both exist the same word
    #         td[word] = int(d[word])-int(d1[word])
    #     elif word in d1:
    # # only exist in d1
    #         td[word] = -int(d1[word])
    #     elif word in d: 
    # # only exist in d
    #         td[word] = int(d[word])
    # return 'Counter(' + str(td) + ')'
    

