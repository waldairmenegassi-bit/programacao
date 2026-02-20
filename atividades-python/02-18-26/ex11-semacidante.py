tempo = int(input("dias sem acidentes: "))
ano = 0
mes = 0
dia = 0

while tempo > 0:
    if tempo >=365:
        ano +=1
        tempo = tempo-365
    elif tempo >= 30:
        mes += 1
        tempo = tempo-30
    elif tempo >= 1:
        dia += 1
        tempo = tempo-1

print(ano," anos, ",mes," meses e ",dia," dias sem acidentes")
