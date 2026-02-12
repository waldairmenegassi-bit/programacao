# SIMULA UM BANCO DE DADOS(ARMAZENA OS PRODUTOS)
db = [
    {"id": 1, "nome": "pneu", "preco": 199.99},
    {"id": 2, "nome": "amortecedor", "preco": 350.50},
    {"id": 3, "nome": "oleo de motor", "preco": 45.90},
    {"id": 4, "nome": "filtro de ar", "preco": 29.00},
    {"id": 5, "nome": "bateria 60ah", "preco": 480.00},
    {"id": 6, "nome": "pastilha de freio", "preco": 120.00},
    {"id": 7, "nome": "vela de ignicao", "preco": 15.75},
    {"id": 8, "nome": "limpador de parabrisa", "preco": 35.20},
    {"id": 9, "nome": "fluido de freio", "preco": 22.40},
    {"id": 10, "nome": "correia dentada", "preco": 89.90}
]

# PROCURA PRODUTO PELO ID
def findByID(itemID):
    for item in db:
        if item["id"] == itemID:
            return item # RETORNA O PRODUTO SE FOR ENCONTRADO
    return None # RETORNA NADA CASO NAO SEJA ENCONTRADO

# PROCURA ITENS PELO NOME
def findByName(itemName):
    for item in db:
        if item["nome"].lower() == itemName.lower():
            return item # RETORNA O PRODUTO SE FOR ENCONTRADO
    return None # RETORNA NADA CASO NAO SEJA ENCONTRADO

# REGISTRA UM NOVO PRODUTO
def newProd(itemNome,itemPreco):
    novo_id = db[-1]["id"] + 1 if db else 1 # VAI NO ULTIMO ID DA LISTA; CASO =0 É 1
    novo_item = {"id": novo_id, "nome": itemNome, "preco": itemPreco} # SETA NOVO ITEM
    db.append(novo_item) # INSERE NOVO ITEM NA LISTA

def deleteProd(itemID):
    for i, item in enumerate(db): # PARA CADA ITEM EM DB EXECUTA:
        if item["id"] == itemID:
            db.pop(i) # CASO EXISTA É RMEOVIDO O INDICE
            return True
    return False # CASO NÃO, RETORNA FALSO
    
    # LISTA TODOS OS PRODUTOS
def listProd():
     for item in db: # PARA CADA ITEM EM DB VAI MOSTRAR NOME, ID E PREÇO
        print("==================")
        print("Nome: ", item["nome"])
        print("ID: ", item["id"])
        print("Preço: R$", item["preco"])
         
        
def exibirMenu():
    print("===============")
    print("Digite 1 para LISTAR PRODUTOS")
    print("Digite 2 para CRIAR PRODUTO")
    print("Digite 3 para EXCLUIR PRODUTO")
    print("Digite 4 para PROCURAR PRODUTO")
    print("Digite 5 para SAIR")
    op = int(input(""))

    match op:
        case 1:
            listProd()
        case 2:
            nome = input("Digite nome do produto: ")
            preco = float(input("Preço do produto: "))
            if preco > 0: # CASO PREÇO SEJA MAIOR QUE ZERO PRODUTO É ADICIONADO
                newProd(nome, preco) # CHAMA FUNÇÃO E CRIA PRODUTO
                print("Produto adicionado!") 
            else:
                print("Preço informado deve ser maior que 0!")
        case 3:
            id_del = int(input("Digite o id do produto a ser deletado: "))
            if deleteProd(id_del): # CASO O DELETE DE PRODUTO RETORNE TRUE MOSTRA MENSAGEM DE DEU BOA
                print("Produto deletado com sucesso!")
            else:
                print("ID não encontrado")
        case 4:
            id_busca = int(input("Digite o ID para busca: "))
            item = findByID(id_busca) # BUSCA 
            if item:
                print(f"Achado: {item['nome']} - R$ {item['preco']}")
            else:
                print("Não encontrado.")

op = 0
while op < 5:
    exibirMenu()
  





        



        