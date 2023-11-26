def novoProduto(produtos):
    print("Informe o codigo do produto")
    codigo = input().zfill(13)
    if(any(p["codigo"] == codigo for p in produtos)):
        print("Este código já existe")
        return
    print("Informe o nome do produto")
    nome = input().capitalize()
    print("Informe o preço")
    preco = float(input())
    produtos.append({"codigo": codigo, "nome": nome, "preco": preco})

def deletaProduto(produtos):
    print("Informe o codigo do produto")
    codigo = input().zfill(13)
    for p in produtos:
        if p["codigo"] == codigo:
            produtos.remove(p)
            print("Produto excluído")
            return
    print("Produto não foi encontrado")

def listarProduto(produtos):
    prod = sorted(produtos, key = lambda p: p['preco'])
    i = 0
    for p in prod:
        print(f"Código: {p["codigo"]}")
        print(f"Nome: {p["nome"]}")
        print(f"Preço: {p["preco"]: .2f}")
        i+=1
        if(i % 10 == 0): 
            op = -1
            while(op != 1 and op != 2):
                print("Deseja visualizar mais produtos?")
                print("1- Sim")
                print("2- Não")
                op = int(input())
                if(op == 2):
                    return

def consultarProduto(produtos):
    print("Informe o codigo do produto")
    codigo = input().zfill(13)
    for p in produtos:
        if p["codigo"] == codigo:
            print(f"Nome: {p["nome"]}")
            print(f"Preço: {p["preco"]: .2f}")

