import math #import math module
def get_roots(a, b, c):

    """
    :param a,b,c: int, Determine the roots of delta and calculation equation
    :return: list of int
    
    """
    list=[]
    delta=b**2-4*a*c #Calculating delta
    if delta>0:
        x1=(-b+math.sqrt(delta))/(2*a)
        x2=(-b-math.sqrt(delta))/(2*a) #calculate roots
        list.append(x1)
        list.append(x2)   #Adding roots to the list
    if delta==0:
        x1=-b/(2*a)  #calculate root
        list.append(x1)   #Adding root to the list
    if delta<0:
        pass   #no root
    return list
if __name__ == "__main__":
    print(get_roots(1,3,2))