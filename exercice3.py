class Rational:
    def __init__(self,a,b):
        self.__num = a
        self.__den = b

    def __add__(self, other):
        #print(other) #vérification objet
        a = self.__num
        b = self.__den
        c = other.__num
        d= other.__den
        num = a*d + b*c
        den = b*d
        return (num, den)

    def __sub__(self, other):
        # print(other) #vérification objet
        a = self.__num
        b = self.__den
        c = other.__num
        d = other.__den
        num = a*d - b*c
        den = b*d
        return (num,den)

    def __rsub__(self, other):
        # print(other) #vérification objet
        a = self.__num
        b = self.__den
        c = other.__num
        d = other.__den
        num = c*b - a*d
        den = b*d
        return (num, den)

    def __mul__(self, other):
        # print(other) #vérification objet
        a = self.__num
        b = self.__den
        c = other.__num
        d = other.__den
        num = a*c
        den = b*d
        return (num,den)

    def __truediv__(self, other):
        # print(other) #vérification objet
        a = self.__num
        b = self.__den
        c = other.__num
        d = other.__den
        num = a*d
        den = b*c
        return (num,den)

    def __rtruediv__(self, other):
        # print(other) #vérification objet
        a = self.__num
        b = self.__den
        c = other.__num
        d = other.__den
        num = c*b
        den = a*d
        return (num,den)




if __name__ == '__main__':
    c1 = Rational(1,2)
    c2 = Rational(2,4)
    #c2 = Rational(-1,2)
    #c1 = Rational(1,2)
    #c1 = Rational(1,-2)
    #c2 = Rational(-1,-2)
    c3 = c1 + c2
    c4 = c1 - c2
    c5 = c2 - c1
    c6 = c1 * c2
    c7 = c1 / c2
    c8 = c2 / c1
    print(c3)
    print(c4)
    print(c5)
    print(c6)
    print(c7)
    print(c8)