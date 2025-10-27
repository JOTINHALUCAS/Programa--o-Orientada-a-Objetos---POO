# faça um estoque modular

estoque_comida = {'bolo': 5, 'carne':10, 'sanduba':14, 'cachorro quente':9, 'mortadela':4, 'pão':20,'queijo':12,'empanada':8,'torta':5,'coxinha':10}
estoque_bebidas = {'Água':12, 'Refrigerante':12, 'Suco':12,'Café':12,'Chá':12,'Suco de maracuja':12,'Vinho sem alcool':12,'Leite':12,'Energético':12,'Caipirinha sem alcool':12}


def mostrar_estoque():
    print('----------------- Estoque Comidas ---------------------')
    for chave, valor in estoque_comida.items():
        print(f'{chave}:{valor}')
    print('------------------ Estoque Bebidas --------------------')
    for chave2,valor2 in estoque_bebidas.items():
        print(f'{chave2}:{valor2}')

def adicionar_produto(estoque,nome,quantidade):
    
    if len(nome) > 0 and quantidade > 3 and estoque == 'Bebidas':
        estoque_bebidas[nome] = quantidade
        return estoque_bebidas
    elif len(nome) > 0 and quantidade > 3 and estoque == 'Comidas':
        estoque_comida[nome] = quantidade
        return estoque_comida
    else:
        print('Não deu para adicionar...')

def remover_produto(nome,quantidade):
    
    if nome in estoque_bebidas:
        estoque_bebidas[nome] -= quantidade
    elif nome in estoque_comida:
        estoque_comida[nome] -= quantidade


def consultar_produto(estoque,nome):
    
    if estoque.lower() == 'bebidas':
        if nome in estoque_bebidas:
            quantidade = estoque_bebidas[nome]
            print(f'O nome: {nome} e a quantidade do produto {quantidade}')
    elif estoque.lower() == 'comidas':
        if nome in estoque_comida:
            quantidade = estoque_comida[nome]
            print(f'O nome: {nome} e a quantidade do produto: {quantidade}')
    
def repor_automatico():
    for estoque in (estoque_comida, estoque_bebidas):
        for nome, quantidade in estoque.items():
            if quantidade < 3:
                estoque[nome] += 5
                print(f"{nome} foi colocado +5 unidades.")

def salvar_relatorio():
    with open("estoque.txt", "w") as arq:
        arq.write("COMIDAS:\n")
        for p, q in estoque_comida.items():
            arq.write(f"{p}: {q}\n")
        arq.write("\nBEBIDAS:\n")
        for p, q in estoque_bebidas.items():
            arq.write(f"{p}: {q}\n")
    print("Relatório salvo em estoque.txt")
    

def menu():
    print('-----------------------------------------------------------------------------------------------------------------------------')
    print('1 - Mostrar estoque 2 - Adicionar produto 3 - Remover produto 4 - Consultar produto 5 - Repor automatico 6 - Salvar Relatorio')
    print('-----------------------------------------------------------------------------------------------------------------------------')


while True:
    menu()
    op = input('Dgite um dos números:')
    
    if op == '1':
        mostrar_estoque()
    
    elif op == '2':
        q_estoque = input('Deseja adicionar em qual estoque?')
        nome_produto = input('Digite o nome do novo produto:')
        quantidade_produto = int(input('Digite a quantidade do novo produto:'))
        adicionar_produto(q_estoque,nome_produto,quantidade_produto)
    
    elif op == '3':
        nome_produto= input('Digite o nome do produto:')
        quantidade_produto = int(input('Qual a quantidade do produto que deseja remover?'))
        remover_produto(nome_produto,quantidade_produto)
   
    elif op == '4':
        q_estoque = input('Qual o estoque?')
        nome_prod = input('Digite o nome do produto:')
        consultar_produto(q_estoque,nome_prod)
    
    elif op == '5':
        repor_automatico()
    elif op == '6':
        salvar_relatorio()
        print('Saindo...')
        break
