O módulo ``romanos`` fornece constantes da classe ``Romano`` que são inteiros
expressos em algarismos romanos. Por exemplo::

	>>> from romanos import I, II, III
	>>> int(I)
	1
	>>> I + II
	III
	>>> 1 + II
	III
	>>> II + 1
	III
	>>> 3 * II
	6
	>>> II * 3
	6
