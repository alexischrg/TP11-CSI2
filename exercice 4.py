class Duree:
    def __init__(self,h=0,m=0,s=0):
        self.__heure = h
        self.__minute = m
        self.__seconde = s

    def afficher(self):
        h = self.__heure
        m = self.__minute
        s = self.__seconde
        print(h,'h',m,'m',s,'s')

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




dur1 = Duree(13,15,50)
dur2 = Duree(1,50, 12)
durtot = dur1 + dur2
dur1.afficher()
durtot.afficher()