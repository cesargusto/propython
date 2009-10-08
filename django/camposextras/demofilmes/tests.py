# coding: utf-8

"""

-------------------------
Carga da massa de testes
-------------------------

Inicialmente carregamos uma amostra de dois filmes, e verificamos a carga::

    >>> from django.core import management
    >>> management.call_command('loaddata', 'dois-filmes.json', verbosity=0)

    >>> from models import Filme, Credito
    >>> len(Filme.objects.all())
    2
    >>> len(Credito.objects.all())
    11
    >>> print Filme.objects.all().order_by('titulo')[0]
    Apocalypse Now (1979)

--------------------------------------------
Uso de `reverse` para evitar caminhos fixos
--------------------------------------------

Acessamos as views sempre pelo nome, evitando o uso de caminhos fixos, para
que mudanças na configuração do `urls.py` da instância do Django (acima da 
aplicação) não alterem o funcionamento dos testes. Para isso usamos afunção
`reverse`, que transforma assinaturas de views (nomes e argumentos) em 
caminhos::

    >>> from django.core.urlresolvers import reverse
    >>> reverse('demofilmes.indice')[0]
    '/'
    
Nota: O máximo que a gente consegue testar sem depender da configuração do 
ROOT_URLCONF é que o caminho retornado começa com '/', pois isso é sempre
verdade. Examinar o caminho completo introduzira uma fragilidade no teste.

-------------------------------------------------
Acesso à página índice da aplicação `demofilmes`
-------------------------------------------------

    >>> from django.test.client import Client
    >>> c = Client()
    >>> resp = c.get(reverse('demofilmes.indice'))
    
Podemos verificar o código HTTP da resposta::

    >>> resp.status_code
    200
    
Ou a presença de uma string no conteúdo da resposta::    
    
    >>> 'Apocalypse' in resp.content
    True
    
Ou ainda acessar o contexto que foi usado para gerar a resposta::    
    
    >>> for i in resp.context['object_list']: print i.pk, i
    1 Apocalypse Now (1979)
    2 Não por acaso (2007)
    
----------------------------------------------
Acesso à página de detalhes do primeiro filme
----------------------------------------------

    >>> resp = c.get(reverse('demofilmes.ver',args=(1,)))
    >>> 'Coppola' in resp.content and 'Brando' in resp.content
    True
    
Nota: O cliente de HTTP do Django é mais limitado que o do zope.testbrowser.
Por exemplo, ele não facilita explorar os elementos da página (no 
zope.testbrowser tem métodos como `getForm`, `getLink`, `getControls`...).
    
"""

from django.test import TestCase

from models import Filme, Credito

class CarregaVerifica(TestCase):
    ''' faz o mesmo que o trecho inicial do doctest acima '''
    fixtures = ['dois-filmes.json']
    
    def test_carga(self):
        ''' verifica se a massa de testes foi carregada '''
        self.assertEqual(len(Filme.objects.all()), 2)
        self.assertEqual(len(Credito.objects.all()), 11)

    def test_primeiro_filme(self):
        self.assertEqual(unicode(Filme.objects.all().order_by('titulo')[0]),
                         u'Apocalypse Now (1979)')
