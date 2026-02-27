import random

ingrediente = {
    "queijo" : bool,
    "presunto" : bool,
    "burguer" : bool,
    "molho" : bool,
    "picles" : bool,
    "alface" : bool,
    "tomate" : bool,
}

def pedido():
    for chave in ingrediente:
        ingrediente[chave] = random.choice([True, False]) 
        

