class Vector:
    def __init__(self,x):
        """
        constructor of the Vector class
        input:
        x - list or tuple of lenght
        sets:
        self.x - tuple: the vector values
        self.n - vector length
        >>> v = Vector([1,2,3])
        """
        self.x=()
        self.n=len(x)
        for i in x:
            self.x+=(i,)


    def scaled_copy(self,scale):
        """ 
        Isotropic scaling, scalar multiplication, in fact
        https://en.wikipedia.org/wiki/Scaling_(geometry)
        >>> v = Vector([1,2,3])
        >>> v2 = v.scaled_copy(3)
        >>> v.x
        (1, 2, 3)
        >>> v2.x
        (3, 6, 9)
        """
        x=self.x
        self.x=()
        for i in x:
            self.x+=(i*scale,)
        return self.x
        
     

    def __add__(self,other):
        """
        overloading the + operator
        :return: Vector object result of the addition, None if not possible (not compatible vectors)
        """
        x=()
        if self.n==other.n:
            for s,o in zip(self.x,other.x):
                x+=(s+o,)
            return x
        else:
            return None
if __name__ == "__main__":
    v = Vector([1,2,3])
    v2 = v.scaled_copy(3)
    print(v2.x)

       
