class Contato:

    def __init__(self, nome, telefone, email):
        self.nome = nome
        self.telefone = telefone
        self.email = email


class Agenda:

    def __init__(self) -> None:
        self.contatos = []

    def adicionar_contatos(self, nome, telefone, email):
        novo_contato = Contato(nome, telefone, email)
        self.contatos.append(novo_contato)
        print(f'Contato salvo com sucesso!')

    def editar_contato(self, nome, novo_telefone, novo_email):
        for contato in self.contatos:
            if contato.nome == nome:
                contato.telefone = novo_telefone
                contato.email = novo_email
                print('Contato editado com sucesso')

    def excluir_contato(self, nome):
        for contato in self.contatos:
            if contato.nome == nome:
                self.contatos.remove(contato)
                print('Contato excluído com sucesso!')
            else:
                print('Contato não encontrado')

    def pesquisar_contatos(self, nome):
        for contato in self.contatos:
            if contato.nome.upper() == nome.upper():
                print('Resultado da busca')
                print(f'Nome: {contato.nome}, Telefone: {contato.telefone}')
            else:
                print(f'Contato com o nome {nome} não foi encontrado')

    def mostrar_todos_contatos(self):
        for contato in self.contatos:
            print(
                f'Nome: {contato.nome}, Telefone: {contato.telefone}, Email: {contato.email}')
            print(end=' ')


agenda = Agenda()
agenda.adicionar_contatos('Eric', '79991650182', 'eric@gmail.com')
agenda.adicionar_contatos('João', '79991650182', 'eric@gmail.com')
agenda.mostrar_todos_contatos()
agenda.editar_contato('Eric', '555555', 'ericjesus@gmail.com')

agenda.mostrar_todos_contatos()
agenda.excluir_contato('Eric')
agenda.mostrar_todos_contatos()
agenda.pesquisar_contatos('João')
