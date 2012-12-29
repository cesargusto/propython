========================
Demostração de __slots__
========================

Normalmente Python utiliza um dicionário chamado ``__dict__`` para gerenciar
os atributos das classes que você cria. Veja por exemplo::

	>>> class Pessoa(object):
	...     idade = 0
	...
	>>> dir(Pessoa)
	>>> p = pessoa()
