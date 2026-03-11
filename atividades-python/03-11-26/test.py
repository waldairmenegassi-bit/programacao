# APENAS TRABALHO DE DESCOBRIR MEDIDA REAL
import os


pasta = os.path.dirname(__file__)
arquivo = os.path.join(pasta, "bimbim.txt") # Abre o arquivo com texto

with open(arquivo, "r", encoding="utf-8") as texto: # Le o arquivo 
    retorno = texto.readlines() # Salva em retorno cada linha com seu texto
    for char in retorno[0]: 
        print("Retorno: ",retorno)
        