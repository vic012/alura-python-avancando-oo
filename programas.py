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

class Serie(Programa):
	
	def __init__(self, nome, ano, temporadas):
		super().__init__(nome, ano)
		self.temporadas = temporadas

'''filme = Filme('homem aranha', 2002, 120)
filme.dar_like()
print(f'{filme.nome} - {filme.duracao} : {filme.likes}')'''