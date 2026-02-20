qpao =   int(input("Quantidade paes vendidos: "))
qbroa = int(input("Quntidade de broas vendidas: "))


ppao = qpao*0.12
pbroa = qbroa*1.5
total = ppao + pbroa
poupa = total * 0.1
arrecado = total-poupa
print("foi arrecadado {:.2f} R$ e {:.2f}R$ foram a popuança".format(arrecado,poupa))