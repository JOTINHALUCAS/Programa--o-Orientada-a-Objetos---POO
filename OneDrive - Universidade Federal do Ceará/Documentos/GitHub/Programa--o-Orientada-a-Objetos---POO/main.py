class Conta:
    def __init__(self,numero,titular,saldo):
        self.numero = numero
        self.saldo = saldo
        self.titular = titular

    def creditar(self,valor):
        self.saldo += valor
    
    def debitar(self,valor):
        if valor <= self.saldo:
            self.saldo -= valor
        else:
            print('Não foi possível')
    
    def mostrar_Saldo(self):
        print(f"O saldo da conta é {self.saldo}")

    
        
class Banco:
    def __init__(self,nome):
        self.nome_banco = nome
        self.lista_contas = []
    
    def adicionar_conta(self,conta):
        self.lista_contas.append(conta)

    def creditar(self,valor):
        self.saldo += valor
    
    def transferir(self,conta_origem, conta_destino, valor):
        if conta_origem.saldo >=  valor:
            conta_origem.debitar(valor)
            conta_destino.creditar(valor)
            print(f"Transação de {valor:.2f} realizada com sucesso")
        else:
            print("Saldo não suficiente")
    
    def saldo(self,conta):
        conta.mostrar_Saldo()

if __name__ == "__main__":

    banco = Banco('Banco geral')

    c1 = Conta(1, "João", 1000)
    c2 = Conta(2, "Maria", 500)

    banco.adicionar_conta(c1)
    banco.adicionar_conta(c2)

    banco.saldo(c1)
    banco.saldo(c2)

   
    banco.transferir(c1,c2, 200)

    banco.saldo(c1)
    banco.saldo(c2)

