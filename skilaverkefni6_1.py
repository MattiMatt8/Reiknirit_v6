# Matthías Ólafur

class Heildun:
    def __init__(self,fall):
        fall2 = []
        b = 0
        for x in range(len(fall)):
            s = fall[x]
            if (fall[b] == "+"):
                b += 1
            if ((s == "-" or s == "+") and (x != 0)):
                s2 = fall[b:x]
                fall2.append(self.splitta(s2))
                b = x
            elif x == len(fall) - 1:
                s2 = fall[b:x + 1]
                fall2.append(self.splitta(s2))
                b = x
        self.heilda(fall2)
    def splitta(self,s2):
        lok = []
        for i in range(len(s2)):
            s3 = s2[i]
            if (s3 == "x"):
                if (i != 0):
                    if (s2[0:i] == "-"):
                        lok.append(-1.0)
                    else:
                        lok.append(float(s2[0:i]))
                else:
                    lok.append(1.0)
                lok.append(s2[i])
                if (i != len(s2) - 1):
                    lok.append(float(s2[i + 1:len(s2)]))
                else:
                    lok.append(1.0)
                break
            if (i == len(s2) - 1):
                lok.append(s2)
        return lok
    def heilda(self,fall):
        heildad = []
        for x in range(len(fall)):
            s = fall[x]
            if len(s) == 1:
                heildad.append([int(s[0]),"x"])
            else:
                s[2] += 1
                s[0] /= s[2]
                heildad.append(s)
        self.fallHeildad = heildad
    def reikna(self,xHnit):
        heild = 0
        for x in range(len(self.fallHeildad)):
            s = self.fallHeildad[x]
            if (len(s) == 2):
                heild += s[0] * float(xHnit)
            else:
                heild += s[0] * (float(xHnit)**s[2])
        return round(heild,2)
    def reiknaFlatarmal(self,x1,x2):
        reiknad = self.reikna(x1)
        reiknad2 = self.reikna(x2)
        flatarmal = reiknad - reiknad2
        return flatarmal
    def flatarmalFalla(self,heildanFall,x1,x2):
        fall1Flatarmal = self.reiknaFlatarmal(x1,x2)
        fall2Flatarmal = heildanFall.reiknaFlatarmal(x1,x2)
        return abs(fall1Flatarmal - fall2Flatarmal)

fall1 = input("Sláðu inn fall f(x): ")
fall2 = input("Sláðu inn fall g(x): ")
x1 = input("Sláðu inn x efri mörk: ")
x2 = input("Sláðu inn x neðri mörk: ")

fall1Heildun = Heildun(fall1)
fall2Heildun = Heildun(fall2)
flatarmal = fall1Heildun.flatarmalFalla(fall2Heildun,x1,x2)

print("\nFlatarmál milli fallanna er:",flatarmal)