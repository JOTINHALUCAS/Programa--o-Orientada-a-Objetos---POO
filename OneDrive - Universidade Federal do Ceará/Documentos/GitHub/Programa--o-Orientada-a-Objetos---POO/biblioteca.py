class Livro:
    def __init__(self,titulo,autor,ano):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.disponivel = True

    def emprestar(self):
        if self.disponivel == True:
            self.disponivel = False
            print(f'{self.titulo} foi emprestado')
        else:
            print('Ele não está disponível')

    def devolver(self):
        if self.disponivel == False:
            self.disponivel = True
            print(f'O livro {self.titulo} foi devolvida com sucesso')
        else:
            print('Nada ')

class Usuario:
    def __init__(self,nome,id_user):
        self.nome = nome
        self.id_user = id_user
        self.livros_emprestados = []

    def emprestar_livro(self,livro):
        if livro.disponivel:
            livro.emprestar()
            self.livros_emprestados.append(livro)
        else:
            print(f'{livro.titulo} não está disponível no momento.')

    def devolver_livro(self,livro):
        if livro in self.livros_emprestados:
            livro.devolver()
            self.livros_emprestados.remove(livro)
        else:
            print(f'{self.nome} não possui o livro "{livro.titulo}".')
        
if __name__ == '__main__':
    sistema_livros = Usuario('João',1)

    livro1 = Livro('Cabeça fria Coração quente','Abel Ferreira',2022 )
    livro2 = Livro('Biblia','Jesus',1600)
        
    sistema_livros.emprestar_livro(livro1)
    sistema_livros.emprestar_livro(livro2)

    sistema_livros.devolver_livro(livro1)

    
    