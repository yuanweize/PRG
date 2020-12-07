# def print_left_triangle(n_rows, char):
#     for i in range(n_rows):
#         # i+=1
#         print(char * (i+1))

# if __name__=='__main__':
#     print_left_triangle(10,"T")



# def print_left_triangle(n_rows, char):
#     for i in range(1,n_rows+1):
#         print(char * i)

# if __name__=='__main__':
#     print_left_triangle(4,"T")

# def print_left_triangle(n_rows, char):
#     for i in range(1,n_rows+1):
        
#         print(' '*(n_rows-i)+char * i)

# if __name__=='__main__':
#     print_left_triangle(10,"T")

# n=10
# d={}
# for i in range(1,n+1):
#     d[i]=i*i
# print(d)


# sampleDict = {
# 'Physics': 82,
# 'Math': 65,
# 'History': 75
# }
# sorted(sampleDict)
# sorted(sampleDict,key=sampleDict.get)



inventory = {
    'gold' : 500,
    'pouch' : ['flint', 'twine', 'gemstone'],
    'backpack' : ['xylophone','dagger', 'bedroll','bread loaf']
}
inventory['pocket'] = ['seashell', 'strange berry', 'lint']
print(inventory)
# inventory['backpack'].sort()
# print(inventory)
# inventory['backpack'].remove('dagger')
# print(inventory)
# inventory['gold']+=50
# print(inventory)


# def pig_latin(word):
#     a=word[1:]+word[0:1]
#     print(a)

# if __name__=='__main__':
#     pig_latin('python')