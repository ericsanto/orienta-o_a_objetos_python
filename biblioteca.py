class Livro:

    def __init__(self) -> None:
        self.nome = ''
        self.autor = ''
        self.ano = ''
        self.num_identificacao = 0


class Biblioteca:

    def __init__(self) -> None:
        self.livros = []
        self.emprestado = False
        self.novo_livro = ''

    def cadastrar_livro(self, nome: str, autor: str, ano: str, num_identificacao: int) -> None:
        self.novo_livro = Livro()
        self.novo_livro.nome = nome
        self.novo_livro.autor = autor
        self.novo_livro.ano = ano
        self.novo_livro.num_identificacao = num_identificacao

        self.livros.append(self.novo_livro)
        print(f'Livro {nome} cadastrado com sucesso')

    def exibir_livros_cadastrados(self):
        for livro in self.livros:
            print(
                f'Nome: {livro.nome} | Autor: {livro.autor} | Ano: {livro.ano} | Num.Identificacao: {livro.num_identificacao}')

    def exibir_livro_por_nome(self, nome: str) -> None:
        for livro in self.livros:
            if livro.nome == nome:
                print('Livro encontrado')
                print(
                    f'Nome: {livro.nome} | Autor: {livro.autor} | Ano: {livro.ano} | Num.Identificacao: {livro.num_identificacao}')

    def emprestar_livro(self, nome):
        if self.novo_livro in self.livros:
            if not self.emprestado:
                self.__mensagem_de_emprestimo(nome)
                self.emprestado = True
            else:
                self.__mensagem_de_erro_emprestimo(nome)
        else:
            self. __mensagem_de_erro_nao_tem_livro_na_biblioteca(nome)

    def devolver_livro(self, nome):
        if self.novo_livro in self.livros:
            if self.emprestado:
                self.__mensagem_de_emprestimo(nome)
                self.emprestado = False
            else:
                self.__mensagem_de_erro_emprestimo(nome)
        else:
            self. __mensagem_de_erro_nao_tem_livro_na_biblioteca(nome)

    def __mensagem_de_emprestimo(self, nome: str) -> None:
        print(f'Você recebeu o livro {nome} emprestado')

    def __mensagem_de_erro_emprestimo(self, nome: str):
        print(f'O livro{nome} está emprestado')

    def __mensagem_de_erro_nao_tem_livro_na_biblioteca(self, nome):
        print(f'O livro {nome} não está cadastrado na biblioteca')


bi = Biblioteca()
bi.cadastrar_livro('Dom Casmurro', 'Machado de Assis', '1950', 5)
bi.cadastrar_livro('A Moreninha', 'Machado de Assis', '1954', 3)

bi.exibir_livros_cadastrados()
bi.exibir_livro_por_nome('Dom Casmurro')
bi.emprestar_livro('Dom Casmurro')
