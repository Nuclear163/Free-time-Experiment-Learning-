import math
v = int(input("Vnesi hitrost topovske kroglje"))
alfa = int(input("Vnesi kot pod katerim top izstreli topovsko kroglo"))
alfa = 2* alfa
alfar = math.radians(alfa)


s = ((math.pow(v,2))*(math.sin(alfar))/(10))
print("Topovska kroglja je dosegla dolžino: ",s ," Metrov.")

