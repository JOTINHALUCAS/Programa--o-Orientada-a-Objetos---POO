from .campus import Campus, Curso


class Gerencia:
    def __init__(self):
        self.campi = []


    def criar_campus(self):
        nome = input('Digite o nome do campus: ')
        novo_campus = Campus(nome)
        self.campi.append(novo_campus)
        print('Campus criado com sucesso!')


    def listar_campus(self):
        if not self.campi:
            print('Nenhum campus cadastrado.')
            return
        
        print('\n--- Lista de Campi ---')
        for i, c in enumerate(self.campi):
            print(f'{i} - {c.nome}')


    def atualizar_campus(self):
        self.listar_campus()

        if not self.campi:
            return
        
        try:
            indice = int(input('Digite o índice do campus que deseja atualizar: '))
            if 0 <= indice < len(self.campi):
                novo_nome = input('Digite o novo nome do campus: ')
                self.campi[indice].nome = novo_nome
                print('Campus atualizado com sucesso!')
            else:
                print('Índice inválido.')
        except ValueError:
            print('Digite um índice válido.')


    def excluir_campus(self):
        self.listar_campus()

        if not self.campi:
            return

        try:
            indice = int(input('Escolha o campus que deseja excluir: '))
            if 0 <= indice < len(self.campi):
                self.campi.pop(indice)
                print('Campus removido!')
            else:
                print('Índice inválido.')
        except ValueError:
            print('Digite um índice válido.')

    # --------------------------------------
    # CURSOS
    # --------------------------------------

    def criar_curso(self):
        self.listar_campus()

        if not self.campi:
            print('Nenhum campus disponível.')
            return

        try:
            indice = int(input('Escolha o campus para adicionar o curso: '))
            if 0 <= indice < len(self.campi):
                nome = input('Nome do curso: ')
                codigo = input('Código do curso: ')
                novo_curso = Curso(nome, codigo)
                self.campi[indice].adicionar_curso(novo_curso)
                print('Curso criado com sucesso!')
            else:
                print('Índice inválido.')
        except ValueError:
            print('Digite um índice válido.')

    def listar_cursos(self):
        self.listar_campus()

        if not self.campi:
            return

        try:
            indice = int(input("Escolha o campus para listar os cursos: "))
            if 0 <= indice < len(self.campi):
                campus = self.campi[indice]

                print(f"\n--- Cursos do Campus {campus.nome} ---")

                if not campus.cursos:
                    print("Nenhum curso cadastrado.")
                else:
                    campus.listar_cursos()
            else:
                print("Índice inválido.")
        except ValueError:
            print("Digite um número válido.")

    def atualizar_curso(self):
        self.listar_campus()

        if not self.campi:
            return
        
        try:
            indice_campus = int(input("Escolha o campus: "))
            if 0 <= indice_campus < len(self.campi):
                campus = self.campi[indice_campus]

                campus.listar_cursos()

                if not campus.cursos:
                    print("Esse campus não possui cursos.")
                    return

                indice_curso = int(input("Escolha o curso para atualizar: "))

                if 0 <= indice_curso < len(campus.cursos):
                    novo_nome = input("Novo nome do curso: ")
                    novo_codigo = input("Novo código: ")

                    curso = campus.cursos[indice_curso]
                    curso.nome = novo_nome
                    curso.codigo = novo_codigo

                    print("Curso atualizado com sucesso!")
                else:
                    print("Índice inválido.")
            else:
                print("Índice inválido.")

        except ValueError:
            print("Digite um número válido.")

    def excluir_curso(self):
        self.listar_campus()

        if not self.campi:
            return
        
        try:
            indice_campus = int(input("Escolha o campus: "))
            if 0 <= indice_campus < len(self.campi):
                campus = self.campi[indice_campus]

                campus.listar_cursos()

                if not campus.cursos:
                    print("Esse campus não possui cursos.")
                    return

                indice_curso = int(input("Escolha o curso que deseja excluir: "))

                if 0 <= indice_curso < len(campus.cursos):
                    campus.remover_curso(indice_curso)
                    print("Curso removido com sucesso!")
                else:
                    print("Índice inválido.")
            else:
                print("Índice inválido.")

        except ValueError:
            print("Digite um número válido.")
