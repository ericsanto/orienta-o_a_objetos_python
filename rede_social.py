class RedeSocial:

    def __init__(self) -> None:
        self.usuarios = {}

    def cadastrar_usuarios(self, nome: str) -> None:
        if self.__verificar_dados(nome):
            self.__verificar_se_usuario_esta_cadastrado(nome)

    def adicionar_amigo(self, usuario: str, amigo: str) -> None:
        if self.__verificar_dados(amigo):
            self.__verificar_se_amigo_ja_existe(usuario, amigo)

    def postar_conteudo(self, usuario: str, mensagem: str):
        if self.__verificar_dados(usuario):
            if usuario in self.usuarios:
                self.usuarios[usuario]['posts'].append(mensagem)
                print('Conteúdo postado!')
            else:
                print('Você não possui uma conta. Acesse a página e cadastre-se')

    def buscar_usuarios(self, usuario: str, nome: str) -> None:
        if self.__verificar_dados(usuario) and self.__verificar_dados(nome):
            if usuario in self.usuarios and nome in self.usuarios:
                print('Usuário encontrado')
            else:
                print('Usuário não encontrado')

    def __verificar_dados(self, nome: str) -> bool:
        if isinstance(nome, str):
            return True
        else:
            return False

    def __verificar_se_usuario_esta_cadastrado(self, nome: str) -> None:
        if nome not in self.usuarios:
            self.usuarios[nome] = {'amigos': [], 'posts': []}
            print('Usuário cadastrado!')
        else:
            print(f'Usuário com nome {nome} já existe')

    def __verificar_se_amigo_ja_existe(self, usuario: str, amigo: str) -> None:
        if usuario in self.usuarios and amigo in self.usuarios:
            self.usuarios[usuario]['amigos'].append(amigo)
            self.usuarios[amigo]['amigos'].append(usuario)
            print('Vocês se tornaram amigos')
        else:
            print('Usuário não encontrado')

    def get_consultar_posts(self, usuario: str) -> None:
        for post in self.usuarios[usuario]['posts']:
            print(post)


rede = RedeSocial()

rede.cadastrar_usuarios('Eric')
rede.cadastrar_usuarios('Tafarel')
rede.adicionar_amigo('Eric', 'Tafarel')
rede.postar_conteudo('Tafarel', 'SAI QUE É SUA, TAFAREL')
rede.get_consultar_posts('Tafarel')
rede.buscar_usuarios('Tafarel', 'Lucas')
rede.comentar_posts('Eric', 'Tafarel', 'grande goleiro', 0)
