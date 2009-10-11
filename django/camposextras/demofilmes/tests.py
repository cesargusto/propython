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
    >>> cli = Client()
    >>> resp = cli.get(reverse('demofilmes.indice'))
    
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

A primeira linha a seguir faz algo como `get('/demo/ver/1/')`::

    >>> resp = cli.get(reverse('demofilmes.ver',args=(1,)))
    >>> all(x in resp.content for x in ('Coppola','Brando','Duvall','Sheen'))
    True
    >>> resp.context['object']
    <Filme: Apocalypse Now (1979)>
    >>> creditos = list(resp.context['object'].creditos())
    >>> len(creditos)
    5
    >>> for c in creditos: print '%8s %s' % (c['papel'], c['nome'])
     diretor Francis Coppola
    produtor Francis Coppola
        ator Marlon Brando
        ator Robert Duvall
        ator Martin Sheen

-------------------------------------------------------
Cadastro básico de um filme, view 'demofilmes.simples'
-------------------------------------------------------

Colocamos os dados na view do cadastro simples, verificamos o redirect 
e inspecionamos os dados direto no banco::

    >>> valores = dict(titulo='Das Boot', ano='1981')
    >>> resp = cli.post(reverse('demofilmes.simples'), valores, follow=True)
    >>> resp.redirect_chain
    [('http://.../ver/3/', 302)]
    >>> Filme.objects.get(**valores)
    <Filme: Das Boot (1981)>

---------------------------------------------------------
Cadastro básico de um filme, view 'demofilmes.cadastrar'
---------------------------------------------------------

Mesmo esquema do teste acima: post, redirect e consulta para confirmar. 
Aqui o post é mais complicado por causa do uso de formsets, que usam 
alguns campos hidden::

    >>> valores = dict(titulo='2001, A Space Odyssey', ano='1968')
    >>> dados = {'credito_set-TOTAL_FORMS':'3', 'credito_set-INITIAL_FORMS':'0'}
    >>> dados.update(valores)
    >>> resp = cli.post(reverse('demofilmes.cadastrar'), dados, follow=True)
    >>> resp.redirect_chain
    [('http://.../ver/4/', 302)]
    >>> filme = Filme.objects.get(**valores)
    >>> filme
    <Filme: 2001, A Space Odyssey (1968)>
    >>> list(filme.creditos())
    []
    
-----------------------------------------------------------
Cadastro completo de um filme, view 'demofilmes.cadastrar'
-----------------------------------------------------------

Mesmo esquema do teste acima: post, redirect e consulta para confirmar. 
Aqui o post é mais complicado por causa do uso de formsets, que usam 
alguns campos hidden::

    >>> v_filme = dict(titulo='Brazil', ano='1985')
    >>> v_creds = {'credito_set-0-nome':'Terry Gilliam',
    ...   'credito_set-0-papel':'diretor'}
    >>> v_creds.update({'credito_set-1-nome':'Jonathan Pryce', 
    ...   'credito_set-1-papel':'ator'})
    >>> v_creds.update({'credito_set-2-nome':'Robert De Niro', 
    ...   'credito_set-2-papel':'ator'})
    >>> dados = {'credito_set-TOTAL_FORMS':'3', 'credito_set-INITIAL_FORMS':'0'}
    >>> dados.update(v_filme.items()+v_creds.items())
    >>> resp = cli.post(reverse('demofilmes.cadastrar'), dados, follow=True)
    >>> resp.redirect_chain
    [('http://.../ver/5/', 302)]
    >>> filme = Filme.objects.get(**v_filme)
    >>> filme
    <Filme: Brazil (1985)>
    >>> for c in filme.creditos(): print '%8s %s' % (c['papel'], c['nome'])
     diretor Terry Gilliam
        ator Jonathan Pryce
        ator Robert De Niro
    
    
Nota: O cliente de HTTP do Django é mais limitado que o do zope.testbrowser.
O zope.testbrowser tem métodos como `getForm`, `getLink`, `getControls` etc,
que facilitam muito explorar as páginas geradas. Realmente ele serve para 
verificar as funções de view, mas não o HTML gerado, como diz na documentação.
    
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
