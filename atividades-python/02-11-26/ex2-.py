contador = 1
while contador <= 4:
    nota = float(input("Digite a nota do {contador}° aluno: "))
    soma_notas +=nota
    contador+=1
media = soma_notas/contador
print("Media:",media)