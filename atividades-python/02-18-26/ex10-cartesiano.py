import math
x1 = float(input("Valor do x1: "))
y1 = float(input("Valor do y1: "))
x2 = float(input("Valor do x2: "))
y2 = float(input("Valor do y2: "))
x = (x1,y1)
y = (x2,y2)
d = math.dist(x,y)
print("Distancia entre o ponto X e Y é de {:.2f}".format(d))