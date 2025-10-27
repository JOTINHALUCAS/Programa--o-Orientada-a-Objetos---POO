class Carro:
    def __init__(self,nome,marca,ano):
        self.nome = nome
        self.marca = marca
        self.ano = ano
        self.disponivel = True
    
    def alugar(self):
        if self.disponivel == True:
            self.disponivel = False
            print(f'O carro {self.nome} foi alugado')

    def vender(self):
        if self.disponivel == True:
            self.disponivel = False
            print('Compra realizada com sucesso.')
        else:
            print(f'Esse carro não está disponivel para venda')



