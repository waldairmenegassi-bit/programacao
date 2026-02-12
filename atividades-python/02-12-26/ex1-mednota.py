contador = 1
while contador <= 4:
    nota = float(input("Digite a nota do {contador}° aluno: "))
    soma_notas +=nota
    contador+=1
    if nota < 0 or nota >10:
        print("NOta invalida. a nota deve estar entre 0 e 10")
        continue
media = soma_notas/contador
print("Media:",media)