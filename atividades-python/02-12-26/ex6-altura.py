h = float(input("Digite a altura em cm: "))
sexo = input("sexo (m ou f): ")

if sexo.upper() == "M":
    kgideal = (72.7*(h/100))-58
    print("Peso ideal para uma homem de {:.2f}m é de {:.2f}kg".format((h/100),kgideal))
elif sexo.upper() =="F":
    kgideal = (62.1*h)-44.7
    print("Peso ideal para uma mulher de {:.2f}m é de {:.2f}kg".format((h/100),kgideal))
else:
    print("Seu sexo não é sexual")
    