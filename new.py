class RedeSocial:
    def __init__(self):
        self.usuarios = {}  # Dicionário para armazenar usuários e suas informações

    def adicionar_usuario(self, nome):
        if nome not in self.usuarios:
            self.usuarios[nome] = {'amigos': set(), 'posts': []}
            print(f'Usuário {nome} cadastrado com sucesso.')
        else:
            print(f'O usuário {nome} já existe.')

    def adicionar_amigo(self, usuario, amigo):
        if usuario in self.usuarios and amigo in self.usuarios:
            self.usuarios[usuario]['amigos'].add(amigo)
            self.usuarios[amigo]['amigos'].add(usuario)
            print(f'{usuario} e {amigo} agora são amigos.')
        else:
            print('Usuário(s) não encontrado(s).')

    def publicar_mensagem(self, usuario, mensagem):
        if usuario in self.usuarios:
            post = {'usuario': usuario, 'mensagem': mensagem, 'comentarios': []}
            self.usuarios[usuario]['posts'].append(post)
            print(f'{usuario} publicou uma mensagem: "{mensagem}"')
        else:
            print('Usuário não encontrado.')

    def comentar_post(self, usuario, post_index, comentario):
        if usuario in self.usuarios and 0 <= post_index < len(self.usuarios[usuario]['posts']):
            post = self.usuarios[usuario]['posts'][post_index]
            post['comentarios'].append(
                {'usuario': usuario, 'comentario': comentario})
            print(f'{usuario} comentou no post: "{comentario}"')
        else:
            print('Usuário ou post não encontrado.')

    def buscar_usuario(self, nome):
        if nome in self.usuarios:
            return self.usuarios[nome]
        else:
            print(f'Usuário {nome} não encontrado.')
            return None


# Exemplo de uso
rede_social = RedeSocial()

rede_social.adicionar_usuario('Alice')
rede_social.adicionar_usuario('Alice')
