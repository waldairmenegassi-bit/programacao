import random
saldo = 500
desistir = False
while desistir == False:

    input("Para apostar tecle enter")
    print("Saldo atual: R$",saldo)

    print("\033[93m========================================================\033[0m")
    valoraposta = float(input("\033[94mDigite o valor para aposta: R$\033[0m"))
    print("\033[93m-----------------------------------------------------------033[0m")
    aposta = int(input("\033[94mQUAL A APOSTA? 1 PARA BRANCO | 2 PARA PRETO\033[0m"))
    print("\033[93m-----------------------------------------------------------033[0m")
    mult = int(input("\033[94mMULTIPLICAR 2X, 3X OU 7X: \033[0m"))
    print("\033[93m========================================================\033[0m")

    if aposta == 1:
        branco = random.randint(1,100)-mult*3
        preto = random.randint(1,100)
        
    elif aposta == 2:
        branco = random.randint(1,100)
        preto = random.randint(1,100)-mult*3
       
    if branco > preto and aposta == 1:
        saldo += valoraposta*mult
        print("\033[32mGRANDE GANHO!!\033[0m")
        print("\033[92m+R${}\033[0m".format(valoraposta*mult))
        print("\033[93m-----------------------------------------------------------033[0m")
    elif preto > branco and aposta == 2:
        saldo += valoraposta*mult
        print("\033[32mGRANDE GANHO!!\033[0m")
        print("\033[92m+R${}\033[0m".format(valoraposta*mult))
        print("\033[93m-----------------------------------------------------------033[0m")
    elif preto < branco and aposta == 2:
        saldo -= valoraposta
        print("\033[31mNÃO FOI HOJE\033[0m")
        print("\033[1;31m-R${}\033[0m".format(valoraposta))
        print("\033[93m-----------------------------------------------------------033[0m")
    elif preto > branco and aposta == 1:
        saldo -= valoraposta
        print("\033[31mNÃO FOI HOJE\033[0m")
        print("\033[1;31m-R${}\033[0m".format(valoraposta))
        print("\033[93m-----------------------------------------------------------033[0m")
    
 
