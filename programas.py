
class Filme:
	
	def __init__(self, nome, ano, duracao):
		self.__nome = nome.title()
		self.ano = ano
		self.duracao = duracao
		self.__likes = 0

	@property
	def nome(self):
		return self.__nome

	@nome.setter
	def nome(self, novo_nome):
		self.__nome = novo_nome.title()

	

class Serie:
	
	def __init__(self, nome, ano, temporadas):
		self.__nome = nome.title()
		self.ano = ano
		self.temporadas = temporadas
		self.__likes = 0

	@property
	def nome(self):
		return self.__nome

	@nome.setter
	def nome(self, novo_nome):
		self.__nome = novo_nome.title()

filme = Filme('homem aranha', 2002, 120)
print(filme.nome)
filme.nome = 'Titan'
print(filme.nome)

serie = Serie('super natural', 2002, 3)
print(serie.nome)
serie.nome = 'terra nova'
print(serie.nome)