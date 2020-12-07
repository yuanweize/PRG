class PointPolar:
    """represents a point in polar coordinates"""

    def __init__(self, r, phi):
        """
        :param r: float, norm of the point
        :param phi: float, angular coordinate
        """
        self.r=r
        self.phi=phi
    def __str__(self):
        """
        >>> p1 = PointPolar(5.1, 0.2)
        >>> print(p1)
        Point: r=5.1, phi=0.2
        """
        return str('Point: r='+str(self.r)+', phi='+str(self.phi))
    def __eq__(self, other):
        """Equality given by both parameters"""
        return other.phi==self.phi and other.r==self.r
    def __mul__(self, other):
        """Multiplication of 2 points"""
        return PointPolar(other.r*self.r,other.phi+self.phi)
    def __truediv__(self, other):
        """Division of 2 points"""
        return PointPolar(self.r/other.r,self.phi-other.phi)
    def __lt__(self, other):
        """Is self < other?"""
        return other.r>self.r
    def __le__(self, other):
        """Is self <= other?"""
        return other.r>=self.r
    def __gt__(self, other):
        """Is self > other?"""
        return other.r<self.r
    def __ge__(self, other):
        """Is self >= other?"""
        return other.r<=self.r
if __name__ == "__main__":
    p1 = PointPolar(5.1, 0.2)
    p2 = PointPolar(5.0, 0.2)
    print(str(p1*p2))
    