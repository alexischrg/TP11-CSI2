class Circle:
    def __init__(self,ray):
        self.__r = ray

    def __add__(self, other):
        return Circle(self.__r + other.__r, self.__r + other.__r)

    def __lt__(self, other):
        return self.__r < other.__r and self.__r <other.__r

    def __gt__(self, other):
        return self.__r > other.__r and self.__r > other.__r

if __name__== '__main__' :
    c1 = Circle(2)
    c2 = Circle(3)
    c3 = c1 + c2
    c4 = c1 < c2
    c5 = c2 > c3
    print(c3)