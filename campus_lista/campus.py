class Curso:
    def __init__(self, nome:str,codigo:int):
        self.codigo = codigo
        self.nome = nome
        self.lista = []

    def __str__(self):
        return f"{self.codigo} - {self.nome}"
    
class Campus:
    def __init__(self,nome:str):
        self.cursos = []
        self.nome = nome
    
    def adicionar_curso(self, curso:str):
        self.cursos.append(curso)

    def listar_cursos(self):
        for i , curso  in enumerate(self.cursos):
            print(f'{i} - {curso}')

    def remover_curso(self, index):
        if 0 <= index < len(self.cursos):
            self.cursos.pop(index)


