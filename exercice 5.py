import numpy as np
class Matrice:
    def __init__(self,data=[]):
        self.__data = data


    def __add__(self, other):
        lst1 = []
        lst2 = []
        lst1.append(self.__data[0][0]+other.__data[0][0])
        lst1.append(self.__data[0][1]+other.__data[0][1])
        lst2.append(self.__data[1][0]+other.__data[1][0])
        lst2.append(self.__data[1][1]+other.__data[1][1])
        return Matrice([lst1,lst2])


    def __iadd__(self, other):
        lst1 = []
        lst2 = []
        lst1.append(other.__data[0][0] + self.__data[0][0])
        lst1.append(other.__data[0][1] + self.__data[0][1])
        lst2.append(other.__data[1][0] + self.__data[1][0])
        lst2.append(other.__data[1][1] + self.__data[1][1])
        return Matrice([lst1, lst2])

    def __sub__(self, other):
        lst1 = []
        lst2 = []
        lst1.append(self.__data[0][0] - other.__data[0][0])
        lst1.append(self.__data[0][1] - other.__data[0][1])
        lst2.append(self.__data[1][0] - other.__data[1][0])
        lst2.append(self.__data[1][1] - other.__data[1][1])
        return Matrice([lst1, lst2])

    def __isub__(self, other):
        lst1 = []
        lst2 = []
        lst1.append(other.__data[0][0] - self.__data[0][0])
        lst1.append(other.__data[0][1] - self.__data[0][1])
        lst2.append(other.__data[1][0] - self.__data[1][0])
        lst2.append(other.__data[1][1] - self.__data[1][1])
        return Matrice([lst1, lst2])

    def __mul__(self, other):
        lst1 = []
        lst2 = []
        lst1.append(self.__data[0][0] * other.__data[0][0] + self.__data[0][1] * other.__data[1][0])
        lst1.append(self.__data[0][0] * other.__data[0][1] + self.__data[0][1] * other.__data[1][1])
        lst2.append(self.__data[1][0] * other.__data[0][0] + self.__data[1][1] * other.__data[1][0])
        lst2.append(self.__data[1][0] * other.__data[0][1] + self.__data[1][1] * other.__data[1][1])
        return Matrice([lst1,lst2])

    def __imul__(self, other):
        lst1 = []
        lst2 = []
        lst1.append(other.__data[0][0] * self.__data[0][0] + other.__data[0][1] * self.__data[1][0])
        lst1.append(other.__data[0][0] * self.__data[0][1] + other.__data[0][1] * self.__data[1][1])
        lst2.append(other.__data[1][0] * self.__data[0][0] + other.__data[1][1] * self.__data[1][0])
        lst2.append(other.__data[1][0] * self.__data[0][1] + other.__data[1][1] * self.__data[1][1])
        return Matrice([lst1, lst2])

    #def __lt__(self, other):
        #<

    #def __gt__(self, other):
        #>

    def __str__(self):
        return ("["+str(self.__data[0][0])+"  "+str(self.__data[0][1])+"\n "+str(self.__data[1][0])+"  "+str(self.__data[1][1])+"]")

    #def __len__(self):
        """
        return("matrice de taille : (",L,",",C,")")"""


if __name__ == '__main__':
    m1 = np.array([(1,2),(1,2)])
    m2 = np.array([(2,1),(2,1)])
    Mat1 = Matrice(m1)
    Mat2 = Matrice(m2)
    t1 = Mat1 + Mat2
    t2 = Mat2 + Mat1
    t3 = Mat1 - Mat2
    t4 = Mat2 - Mat1
    t5 = Mat1 * Mat2
    t6 = Mat2 * Mat1
    print(t1) #[3,3/3,3]
    print(t2) #[3,3/3,3]
    print(t3) #[-1,1/-1,1]
    print(t4) #[1,-1/1,-1]
    print(t5) #après calcul : [6,3/6,3]
    print(t6) #après calcul : [3,6/3,6]