# APENAS TRABALHO DE DESCOBRIR MEDIDA REAL
import os
import sys

pasta = os.path.dirname(__file__)
arquivo = os.path.join(pasta, "bimbim.txt") # Abre o arquivo com texto

escala = ""
escala_direita = ""
escala_esquerda = ""
valor_cota = []
n_de_medidas = int(0)
depois_doisponto = False

with open(arquivo, "r", encoding="utf-8") as texto: # Le o arquivo 
    retorno = texto.readlines() # Salva em retorno cada linha com seu texto
    for char in retorno[0]: # Aramazena a escala
        if char.isnumeric():
            str(char)
            if depois_doisponto:
                escala_direita = escala_direita + char
                escala = escala + char
            else:
                escala = escala+char
                escala_esquerda = escala_esquerda+char
        elif char == ":":
            str(char)
            escala = escala+char
            depois_doisponto = True
        else:
            sys.exit("Escala invalida")

    for linha in retorno:
        for numero in linha: #Armazena a medida ate que haja algo diferente de numero
            if numero.isnumeric():
                str(numero)
                valor_cota[n_de_medidas] = valor_cota[n_de_medidas]+char
            else:
                sys.exit("Medida Invalida")
    texto.close()

cont = int(0)
mr = []
with open(arquivo, "w", encoding="utf-8") as novoarquivo:
    for cota in valor_cota:
        mr[cont] = (escala_direita * cota) / escala_esquerda
        cont += 1
    
    novoarquivo.write("Escala: ",escala)
    cont = int(0)
    for medida_real in mr:
        novoarquivo.write("\nMedida do desenho: ",valor_cota[0]," Medida Real: ",medida_real)