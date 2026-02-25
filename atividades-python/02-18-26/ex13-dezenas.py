n = input("Digite o numero de ate 3 digitos: ")
if len(n) > 3:
    print("NUmero maior que 3 digitos")
else: 
    n= int(n)
    centenas = int(n/100)  
    dezena = int(n/10)

    print("O numero possui {} centenas, {} dezenas e {} unidades".format(centenas,dezena,n))
