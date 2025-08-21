class Televisão:
    def __init__(self, pcanal, min, max):
        self.pcanal = pcanal
        self.cmin = min
        self.cmax = max

    def mudar_canal_parabaixo(self):
        self.canal -=1

    def mudar_canal_paraacima(self):
        self.canal +=1


tv1 = Televisão(pcanal=2, min=2, max=10)
print(tv1.canal)
for x in range (1, 20):
    tv1.mudar_canal_paraacima()
    print(tv1.canal)


tv2 = Televisão(pcanal=10, min=2, max=10)
for x in range (1, 20):
    tv2.mudar_canal_parabaixo()
    print(tv2.canal)
