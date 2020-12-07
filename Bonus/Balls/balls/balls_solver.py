def solve(weigh):
    d={'1':'001','2':'112','3':'220','4':'010','5':'121','6':'202','7':'011','8':'122','9':'200','10':'012','11':'120','12':'201'}
    l=[]
    h=''
    li=''
    d1={}
    heavier1 = weigh([1,4,7,10], [2,5,8,11])
    heavier2 = weigh([1,6,9,12], [2,4,7,10])
    heavier3 = weigh([3,4,9,11], [1,5,7,12])
    l.append(heavier1)
    l.append(heavier2)
    l.append(heavier3)
    for i in l:
        if i == 'left':
            h+='0'
            li+='1'
        elif i == 'right':
            h+='1'
            li+='0'
        else:
            h+='2'
            li+='2'
    for k,v in d.items():
        d1[v]=k
    # return l
    if h in d1:
        return (int(d1[h]), '+')
    else:
        return (int(d1[li]), '-')
