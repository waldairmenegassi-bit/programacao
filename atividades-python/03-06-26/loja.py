mercado = {
    1001: {"nome": "arroz", "preco": 25.90},
    1002: {"nome": "feijao", "preco": 8.50},
    1003: {"nome": "macarrao", "preco": 4.75},
    1004: {"nome": "leite", "preco": 5.20},
    1005: {"nome": "pao", "preco": 7.00},
    1006: {"nome": "ovos", "preco": 12.50},
    1007: {"nome": "carne", "preco": 39.90},
    1008: {"nome": "frango", "preco": 18.90},
    1009: {"nome": "tomate", "preco": 6.40},
    1010: {"nome": "batata", "preco": 5.80}
}

# FUNÇÃO AUXILIAR
# Busca items dentro do dicionario "mercado" pelo ID
def findID(id): 
    itemid = id
    # TRANSFORMA ITEMID EM INTEIRO
    itemid = int(itemid)
    # CASO O INDICE ID ESTEJA EM MERCADO
    if itemid in mercado:
        item = []
        # ITEM RECEBE O ITEM DE INDICE "ITEMID"
        item = mercado[itemid]
        produto = [itemid,item["nome"],item["preco"]]
        # RETORNA PRODUTO COM ID, NOME E PREÇO
        return produto
    #CASO CONTRARIO RETORNA ARRAY DE ERRO
    else:
        error = ["ERRO","4006","Não Identificado o produto"]
        return error
    
def addlist(item):
    itenslist = []
    itenslist.append(item)

def removelist(item):
    pass

def fetchallList():
    pass

def register():
    # RECEBE CODIGO COMO STR E COMPARA TAMANHO
    codigo = input("CODIGO DO PRODUTO: ")
    if len(codigo) > 4 or len(codigo) < 4:
        print("\033[31mCODIGO INVALIDO!\033[0m")
        
    # CASO SEJA CORRETO VERIFICA SE É NUMERICO
    elif codigo.isnumeric():
        int(codigo)
        # PRODUTO RECEBE "PRODUTO[]" DE FindID
        produto = findID(codigo)
        # Caso indice 1 de produto seja ERRO retorna erro ao usuario
        if "ERRO" in produto:
            print("PRODUTO NÃO ENCONTRADO!")
        else:
            print("\033[92m{} - {}\033[0m".format(produto[0],produto[1]))
            print("\033[92mR${:.2f}\033[0m".format(produto[2]))
            input("ENTER para continuar")
    else:
        print("\033[31mCODIGO INVALIDO!\033[0m")


def allregisters():
    pass

def finish():
    pass




menu = True
while menu == True:
    print("===============\nFLUXO DE CAIXA\n===============")
    print("Digite 1 para registrar produtos")
    print("Digite 2 para verificar produtos registrados")
    print("Digite 3 para concluir compra")
    print("Digite 0 para cancelar")
    print("="*20)
    option = int(input("AÇÃO: "))

    match option:
        case 0:
            menu = False
            print("Tenha um bom dia!")
        case 1:
            register()
        case 2:
            allregisters()
        case 3:
            finish()

