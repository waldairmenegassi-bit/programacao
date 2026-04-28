
sombraminha = float(input("Altura sua em CM:"))
alturaminha = float(input("Altura sua sombra em Cm:"))
sombrapredio = float(input("Altura sombra do predio CM:"))

alturapredio = (alturaminha * sombrapredio) / sombraminha

print("Altura do predio é de {:.2f}m".format((alturapredio)/100))
