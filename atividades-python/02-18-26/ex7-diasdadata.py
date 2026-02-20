dia = int(input("dia hoje: "))
mes = int(input("mes hoje: "))

if dia < 1 or dia > 30:
    print("Dia ruim")
elif mes < 1 or mes > 30:
    print("mes ruim")
else:
    tot = dia+(mes*30)
    print("Desde incio do ano foram dias: ",tot)