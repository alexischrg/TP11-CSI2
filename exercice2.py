class Complex:
    def __init__(self,a,b):
        self.__reel = a
        self.__imaginaire = b

    def __add__(self, other):
        a = self.__reel
        b = self.__imaginaire
        c = other.__reel
        d = other.__imaginaire
        reel = a+c
        imaginaire = b+d
        return (reel, imaginaire)

    def __sub__(self, other):
        a = self.__reel
        b = self.__imaginaire
        c = other.__reel
        d = other.__imaginaire
        reel = a-c
        imaginaire = b-d
        return (reel ,imaginaire)

    def __mul__(self, other):
        a = self.__reel
        b = self.__imaginaire
        c = other.__reel
        d = other.__imaginaire
        reel = a*c - b*d
        imaginaire = a*d + b*c
        return (reel , imaginaire)

    def __truediv__(self, other):
        a = self.__reel
        b = self.__imaginaire
        c = other.__reel
        d = other.__imaginaire
        reel = (a*c + b*d)/(c*c + d*d)
        imaginaire = (b*c - a*d)/(c*c + d*d)
        return (reel, imaginaire)

    def __abs__(self):
        valabs = ((self.__reel)**2+(self.__imaginaire)**2)**0.5
        return valabs

    def __eq__(self, other):
        if self.__reel == other.__reel and self.__imaginaire == other.__imaginaire :
            return True
        else:
            return False

    def __ne__(self, other):
        if self.__reel != other.__reel or self.__imaginaire != other.__imaginaire :
            return True
        else:
            return False

    def __str__(self):
        return ("(", str(self.__reel) + "," + str(self.__imaginaire) + ")")

if __name__ == '__main__':
    c1 = Complex(1,2)
    c2 = Complex(2, 1)
    c3 = c1 + c2
    c4 = c1 - c2
    c5 = c1 * c2
    c6 = c1 / c2
    c7 = abs(c1)
    print(c1 == c2)  # False
    print(c1 != c2)  # True
    print(c3)  # (3,3)
    print(c4)  # (-1,1)
    print(c5)  # (0,5)
    print(c6)  # (0.8,0.6)
    print(c7)  # (sqrt(5)) = 2.236...