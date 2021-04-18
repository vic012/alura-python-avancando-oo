#Abstract Base Classes
#Classes abstratas ou ABC's
from abc import ABC

#Servem para garantir que havrão funcionalidades

#Um pacote que quando importado e passado com parâmetro
#Diz para a classe que para ser mutável precisa ter os métodos
#__delitem__, __getitem__, __len__, __setitem__, insert
from collections.abc import MutableSequence
#__abs__, __add__, __complex__, __eq__, __mul__, __neg__,
#__pos__, __pow__, __radd__, __rmul__, __rpow__, __rtruediv__,
#__truediv__, conjugate, imag, real
from numbers import Complex


class Playlist (Complex):
	def __getitem__(self, item):
		super().__getitem__(item)

filmes = Playlist()