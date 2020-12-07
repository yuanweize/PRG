def scalar_mult(sc,v):
    """
    scalar multiplication (scalar * vector)
    :param sc: a scalar mulitplier
    :type sc:int
    :param v: a list - vector

    :return: a list - vector after scalar mult
    """
    li=[]
    #creat a empty list
    for i in v:
        li.append(sc*i)
        #Each element is multiplied by a scalar and stored in the list
    return li
    
def dot_product(u,v):
    """
    vector dot product
    :param u: a list
    :param v: a list
    :return: 
    None if u and v are not compatible
    otherwise a number (float or int)
    """
    c= []
    #creat a empty list for multiplied value
    j = -1
    if len(u)==len(v):
        #Determine whether the length of the list is equal
        for i in range(len(u)):
            j+=1
            c.append(u[i]*v[j])
            #Calculate the multiplied value of the corresponding elements in the two vectors first, and then store it in the list c
        su = sum(c) 
        #Element summation
        return su
    else:
        pass
        #The vector length is not the same, pass

def cross_product(u,v):
    """
    vector cross product, see
    :param u: a list of lenght 3
    :param v: a list of length 3
    :return:
    None if u and v are not compatible
    a list of lenght 3 - cross product of u and v
    """
    cp=[]
    #creat empty list for cross product element
    if len(u) == 3 and len(v)==3:
        #Determine the length of the list
        a=u[1]*v[2]-v[1]*u[2]
        b=v[0]*u[2]-u[0]*v[2]
        c=u[0]*v[1]-v[0]*u[1]
        #Calculate cross product
        cp.append(a)
        cp.append(b)
        cp.append(c)
        #store to list cp
        return cp
    else:
        pass
    #The vector length is not the same or not 3, pass

def are_colinear(u,v):
    """
    testing colinearity of two vectors
    :param u: a list
    :param v: a list
    :return:
    True if u and v are colinear, False otherwise
    """

    c=[]
    #creat a list for store (u/v=k)
    j = -1
    if len(u)==len(v):
        for i in range(len(u)):
            j+=1
            if v[j]==0 and u[i]==v[j]:
                #Determine the case where the denominator is 0, k=1
                c.append(0.0)
            elif v[j]==0 and u[i]!=v[j]:
                #Determine the case where the denominator is 0, k!=1
                return False
            else:
                c.append(float(u[i])/float(v[j]))
                #store value k to list c
        if len(set(c))==2 and 0.0 in c:
            #Exclude the same k value, in two cases, there are 0 and no 0
            return True
        elif len(set(c))>1:
            return False
        else:
            return True
    else:
        return False

def are_perpendicular(u,v):
    """
    testing perpendicularity of two vectors
    :param u: a list
    :param v: a list
    :return:
    True if u and v are perpendicular, False otherwise
    """
    c= []
    j = -1
    if len(u)==len(v):
        #The vector length is different, not vertical
        for i in range(len(u)):
            j+=1
            c.append(u[i]*v[j])
            #Same as dot product calculation method
        a=sum(c)
        if a == 0:
            #dot product is 0, victors vertical
            return True
        else:
            return False
    else:
        return False
