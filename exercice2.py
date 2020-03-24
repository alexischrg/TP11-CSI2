class Complex:
    def __init__(self,a,b):
        self.__reel = a
        self.__imaginaire = b

    def __add__(self, other):
        self.__reel = self.__reel + other.__reel
        self.__imaginaire = self.__imaginaire + other.__imaginaire
        return self.__reel and self.__imaginaire

    def __sub__(self, other):
        self.__reel = self.__reel - other.__reel
        self.__imaginaire = self.__imaginaire - other.__imaginaire
        return self.__reel and self.__imaginaire

    def __mul__(self, other):
        self.__reel = self.__reel * other.__reel
        self.__imaginaire = self.__imaginaire * other.__imaginaire
        return self.__reel and self.__imaginaire

    def __truediv__(self, other):
        self.__reel = self.__reel / other.__reel
        self.__imaginaire = self.__imaginaire / other.__imaginaire
        return self.__reel and self.__imaginaire

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


if __name__ == '__main__':
    c1 = Complex(-2,3)
    c2 = Complex(3,0)
    c3 = c1 + c2
    c4 = c1 - c2
    c5 = c1 * c2
    c5 = c1 / c2
    c6 = abs(c1)
    c1 == c2
    c1 != c2
    print(c3)