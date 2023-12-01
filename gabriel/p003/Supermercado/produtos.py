def addProduto(produtos):
    codigo = input("informe o codigo do produto: ").zfill(13)
    if len(codigo)>13  or  not codigo.isdigit():
        print("Codigo invalido")
        print("Produto não adicionado")
        return
    for p in produtos:
        if p["codigo"] == codigo:
            print("Codigo ja existente")
            print("Produto não adicionado")
            return
    nome  = input("digite o nome do produto: ").capitalize()
    preco = round(float( input("informe o preco: ") ),2)
    produtos.append({"codigo": codigo, "nome": nome, "preco": preco})


def removeProduto(produtos):
    codigo = input("informe o codigo do produto: ").zfill(13)
    for p in produtos:
        if p["codigo"] == codigo:
            produtos.remove(p)
            print("Produto excluido")
            return
    print("Produto não encontrado")

def listaProdutos(produtos):
    produtosOrdenados = sorted(produtos, key=lambda x: x["preco"])
    i=0
    for p in produtosOrdenados:
        print(p)
        i+=1
        if(i%10 == 0):
            op = input("deseja exibir mais produtos? (s/n)").lower()
            if op!="s":
                return
            
def consultarProduto(produtos):
    codigo = input("informe o codigo do produto: ").zfill(13)
    for p in produtos:
        if p["codigo"] == codigo:
            print(p)
            return
    print("Produto não encontrado")
    
    
