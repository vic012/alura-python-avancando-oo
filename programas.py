class Programa:

	def __init__(self, nome, ano):
		self._nome = nome.title()
		self.ano = ano
		self._likes = 0

	@property
	def nome(self):
		return self._nome

	@nome.setter
	def nome(self, novo_nome):
		self._nome = novo_nome.title()

	@property
	def likes(self):
		return self._likes

	def dar_like(self):
		self._likes += 1


class Filme(Programa):
	def __init__(self, nome, ano, duracao):
		#Herda herança da classe mãe e repassa os atributos recebidos
		super().__init__(nome, ano)
		self.duracao = duracao

	#Método especial para mostrar parte da classe textualmente
	def __str__(self):
		return f'Nome: {self._nome} - Ano: {self.ano} - Duração: {self.duracao} minutos - Likes: {self._likes}'

class Serie(Programa):
	
	def __init__(self, nome, ano, temporadas):
		#Herda herança da classe mãe e repassa os atributos recebidos
		super().__init__(nome, ano)
		self.temporadas = temporadas

	#Método especial para mostrar parte da classe textualmente
	def __str__(self):
		return f'Nome: {self._nome} - Ano: {self.ano} - Temporadas: {self.temporadas} - Likes: {self._likes}'

class Playlist(list):
	def __init__(self, nome, programas):
		self.nome = nome
		self._programas = programas

	@property
	def listagem(self):
		return self._programas

	@property
	def tamanho(self):
		return len(self._programas)
	

vingadores = Filme('vingadores - guerra infinita', 2018, 160)
atlanta = Serie('atlanta', 2018, 2)
tmep = Filme('todo mundo em panico', 1999, 100)
demolidor = Serie('demolidor', 2016, 2)

vingadores.dar_like()
vingadores.dar_like()
vingadores.dar_like()
atlanta.dar_like()
atlanta.dar_like()
tmep.dar_like()
tmep.dar_like()
demolidor.dar_like()
demolidor.dar_like()

listinha = [atlanta, vingadores, demolidor, tmep]
minha_playlist = Playlist('fim de semana', listinha)

for programa in minha_playlist.listagem:
    print(programa)

print(f'Tamanho: {len(minha_playlist.listagem)}')