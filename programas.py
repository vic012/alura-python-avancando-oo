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

class Playlist:

	def __init__(self, nome, programas):
		self.__nome = nome
		self.__programas = programas

	def tamanho(self):
		return len(self.__programas)

filme = Filme('homem aranha', 2002, 120)
filme.dar_like()
#print(f'{filme.nome} - {filme.duracao} : {filme.likes}')
serie = Serie('stranger things', 2016, 4)
serie.dar_like()
serie.dar_like()

filmes_e_series = [filme, serie]
playlist = Playlist('Marotona de fim de semana', filmes_e_series)

for programa in playlist:
    print(programa)
