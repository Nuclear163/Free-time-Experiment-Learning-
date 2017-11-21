from random import *

ana = 1
berta = 1
navrsti = "Ana"
zmagovalka =""
while(zmagovalka == ""):
    if navrsti == "Ana":
        while navrsti=="Ana":
            kocka=randint(1, 6)
            if(ana+kocka > 50):
                print("Ana je vrgla prevec: ",ana+kocka)
            else:
                print(kocka)
                ana+=kocka
                print("Ana je vrgla ",kocka," in je na polju :",ana)
            if(kocka == 6):
                navrsti = "Ana"
            else:
                navrsti = "Berta"
            if(ana==berta):
                berta=1
            if(ana==50):
                print("Ana je zmagala")
                zmagovalka="Ana"
                exit()
    if navrsti == "Berta":
        while navrsti=="Berta":
            kocka=randint(1, 6)
            if(berta+kocka > 50):
                print("Berta je vrgla prevec: ", berta + kocka)
            else:
                print(kocka)
                berta += kocka
                print("Berta je vrgla ", kocka, " in je na polju :", berta)
            if (kocka == 6):
                navrsti = "Berta"
            else:
                navrsti = "Ana"
            if(berta==ana):
                ana=1
            if(berta==50):
                print("Berta je zmagala")
                zmagovalka="Berta";
                exit()