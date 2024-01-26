class Livro:

    def __init__(self, titulo, autor, numero_paginas):
        self.titulo = titulo
        self.autor = autor
        self.numero_paginas = numero_paginas
        self.emprestado = False

    def emprestar_livro(self):
        if self.emprestado == False:
            print(f'O livro {self.titulo} está sendo emprestado')
            self.emprestado = True
        else:
            print(f'O livro{self.titulo} já está emprestado')

    def devolver_livro(self):
        if self.emprestado == True:
            print(f'O livro {self.titulo} foi devolvido')
            self.emprestado = False
        else:
            print(f'O livro {self.titulo} não esta emprestado')

    def verificar_disponibilidade_livro(self):
        if self.emprestado == False:
            print(f'O livro {self.titulo} está disponível para emprestimo')
        else:
            print(
                f'O livro {self.titulo} não está disponível para empréstimo, pois já está emprestado')


livro = Livro("O Amor Fala", "Eric", 500)

livro.devolver_livro()
livro.emprestar_livro()
livro.emprestar_livro()
livro.devolver_livro()
livro.verificar_disponibilidade_livro()
