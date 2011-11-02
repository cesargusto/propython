
====================================
Programação funcional em Python
====================================

* (c) 2008-2009 Luciano Ramalho

* luciano@ramalho.org

---------------------------------
Paradigmas
---------------------------------

   Programming language ‘‘paradigms’’ are a moribund and tedious legacy of a bygone age. Modern language designers pay them no respect, so why do our courses slavishly adhere to them? (Shriram Krishnamurthi, author of `Programming Languages: Application and Interpretation`)

- Python é "multi-paradigma"

- Características imperativas, OO e funcionais
  
    
---------------------------------
Em teoria programação funcional é
---------------------------------  
  
    [...] functional programming is a programming paradigm that treats computation as the evaluation of mathematical functions and avoids state and mutable data. It emphasizes the application of functions, in contrast to the imperative programming style, which emphasizes changes in state. (http://en.wikipedia.org/wiki/Functional_programming)


- Definição 2

- Definição 3

-------------------------------------
Na prática, programação funcional usa
-------------------------------------

- funções como objetos de primeira classe

- funções de ordem superior

- avaliação preguiçosa

------------------------------
Funções de primeira classe
------------------------------

- funções são cidadãos de primeira classe na linguagem
  
- uma função pode ser:

  - atribuída a uma variável
  
  - passada como argumento para outra função
  
  - devolvida como resultado de outra função
  
----------------------
Funções como objetos
----------------------

- funções têm atributos

- funções podem ser criadas em tempo de execução

- funções são instâncias de `function`::


    >>> def dobro(n):
    ...    'devolve n vezes 2'
    ...    return n*2
    ... 
    >>> type(dobro)
    <type 'function'>
    >>> function
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    NameError: name 'function' is not defined
    >>> help(type(dobro))


----------------------
Atributos de funções
----------------------

- além de atr comuns (como __repr__), toda função têm:

__closure__, __code__, __defaults__, __dict__, __doc__, __globals__, __name__

- antigamente estes atributos eram chamados func_* (ex: func_code em vez de __code__)

  - os nomes antigos ainda valem no Python 2.6 (são apelidos)

- por exemplo, o __doc__::

    >>> def dobro(x):
    ...     '''devolve 2 vezes x'''
    ...     return 2*x
    ... 
    >>> dobro.__doc__
    'devolve 2 vezes x'
    >>> dobro.func_doc
    'devolve 2 vezes x'
    >>> 

- depois vamos falar sobre os demais

------------------------
Atributos de funções
------------------------

- funções também podem receber atributos arbitrários::

    >>> def mult(x):
    ...     return mult.fator * x
    ... 
    >>> mult.fator = 5
    >>> mult(3)
    15

- no Django este tipo de atributo é usado como anotação


----------------
Referências
----------------

- Hughes, John - `Why Functional Programming Matters` in “Research Topics in Functional Programming” ed. D. Turner, Addison-Wesley, 1990, pp 17–42.

-----------------------------
Perguntas, cursos, mentoria?
-----------------------------

* Luciano Ramalho <luciano@ramalho.org>






