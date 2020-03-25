class Duree:
    def __init__(self,h=0,m=0,s=0):
        self.__heure = h
        self.__minute = m
        self.__seconde = s

    def __add__(self, other):
        h = self.__heure
        m = self.__minute
        s = self.__seconde
        s += other.__seconde
        while s > 60:
            m += 1
            s -= 60
        m += other.__minute
        while m > 60:
            h += 1
            m -= 60
        h += other.__heure
        return Duree(h,m,s)

    def __str__(self):
        return (str(self.__heure) + "h" + str(self.__minute) + "m" + str(self.__seconde) + "s")


if __name__ == '__main__':
    dur1 = Duree(13,15,50)
    dur2 = Duree(1,50, 12)
    durtot = dur1 + dur2
    print(dur1)
    print(durtot)