class Fraction:
    
    def __init__(self, numerator, denominator):
        '''
        input: numerator,denominator
        '''
        self.numerator = numerator # top 
        self.denominator = denominator # bottom
        if denominator == 0:
            raise ZeroDivisionError('Denomeinator can not be ZERO')
        #if denominator is zero then raise error 'Denomeinator can not be ZERO'

    def gcd(self):
        '''
        input: The numerator and denominator of a fraction
        output: gcd number of the fraction
        '''
        m = max(self.denominator, self.numerator)
        n = min(self.denominator, self.numerator)
        # Get the size order of the numerator and denominator
        while m%n:
            m, n = n, m%n
            # Using the Euclidean Algorithm
        return n

    def lcm(self,other):
        '''
        input: The numerator and denominator of two fraction
        output: lcm number of the two fraction
        '''
        m = max(self.denominator, other.denominator)
        n = min(self.denominator, other.denominator)
        # Get the size order of the denominators of the two fractions
        while m%n:
            m, n = n, m%n
            # Using the Euclidean Algorithm
        return self.denominator*other.denominator//n

    def co(self,other):
        '''
        input: The numerator and denominator of the two fraction
        output: float value of the two fraction(for comparison operators)
        '''
        f1=self.numerator/self.denominator
        # Float value of the first fraction
        f2=other.numerator/other.denominator
        # Float value of the second fraction
        return f1,f2

    def __str__(self):
        '''
        input: The numerator and denominator of a fraction
        output: Simplified format fraction
        '''
        gcd=self.gcd()
        # get the gcd of the fraction
        n=int(self.numerator/gcd)
        d=int(self.denominator/gcd)
        # reduction of fraction to a common denominator
        if n%d == 0:
            # The remainder is 0 and the result is an integer.
            ans = str(int(n/d))
        elif self.numerator<0 and self.denominator>0:
            # Exclusion of cases where the numerator and denominator have both a negative sign.
            ans='-'+str(n)+'/'+str(-d)
        else:
            ans=str(n)+'/'+str(d)
        return ans

    def __add__(self,other):
        '''
        input: The numerator and denominator of the two fraction
        output: Simplified results by Class Fraction 
        '''
        lcm=self.lcm(other)
        # get lcm
        n=lcm/self.denominator*self.numerator+lcm/other.denominator*other.numerator
        # Calculate numerator
        return Fraction(n,lcm)

    def __sub__(self,other):
        '''
        input: The numerator and denominator of the two fraction
        output: Simplified results by Class Fraction 
        '''
        lcm=self.lcm(other)
        # get lcm
        n=lcm/self.denominator*self.numerator-lcm/other.denominator*other.numerator
        # Calculate numerator
        return Fraction(n,lcm)

    def __mul__(self,other):
        '''
        input: The numerator and denominator of the two fraction
        output: Simplified results by Class Fraction 
        '''
        n=self.numerator*other.numerator
        # Calculate numerator
        d=self.denominator*other.denominator
        # Calculate denominator
        return Fraction(n,d)

    def __truediv__(self,other):
        '''
        input: The numerator and denominator of the two fraction
        output: Simplified results by Class Fraction 
        '''
        n=self.numerator*other.denominator
        # Calculate numerator
        d=self.denominator*other.numerator
        # Calculate denominator
        return Fraction(n,d)

    def __eq__(self,other):
        '''
        input: Tuple(float value of two fraction) 
        output: Bool value
        '''
        return self.co(other)[0]==self.co(other)[1]
        # Returns a comparison result of the elements in the tuple returned from co

    def __lt__(self,other):
        '''
        input: Tuple(float value of two fraction) 
        output: Bool value
        '''
        return self.co(other)[0]<self.co(other)[1]
        # Returns a comparison result of the elements in the tuple returned from co

    def __le__(self,other):
        '''
        input: Tuple(float value of two fraction) 
        output: Bool value
        '''
        return self.co(other)[0]<=self.co(other)[1]
        # Returns a comparison result of the elements in the tuple returned from co

    def __gt__(self,other):
        '''
        input: Tuple(float value of two fraction) 
        output: Bool value
        '''
        return self.co(other)[0]>self.co(other)[1]
        # Returns a comparison result of the elements in the tuple returned from co
        
    def __ge__(self,other):
        '''
        input: Tuple(float value of two fraction) 
        output: Bool value
        '''
        return self.co(other)[0]>=self.co(other)[1]
        # Returns a comparison result of the elements in the tuple returned from co

if __name__ == "__main__":
    f1 = Fraction(-12,18)
    f2 = Fraction(-4,-9)
    print("f1 = " + str(f1))
    print("f2 = " + str(f2))
    print("f1 + f2 = " + str(f1+f2))
    print("f1 - f2 = " + str(f1 - f2))
    print("f1 * f2 = " + str(f1 * f2))
    print("f1 / f2 = " + str(f1 / f2))
    print("f1 == f2 = " + str(f1==f2))    
    print("f1 < f2 = " + str(f1 < f2))
    print("f1 <= f2 = " + str(f1 <= f2))
    print("f1 > f2 = " + str(f1 > f2))
    print("f1 >= f2 = " + str(f1 >= f2))
