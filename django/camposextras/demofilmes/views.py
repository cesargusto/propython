# coding: utf-8

from django.forms import ModelForm
from django.forms.models import inlineformset_factory
from django.shortcuts import render_to_response, get_object_or_404
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.views.generic.create_update import delete_object

from demofilmes.models import Filme, Credito

def remover(request, object_id):
    return delete_object(request, model=Filme, object_id=object_id,
                         post_delete_redirect=reverse('demofilmes.indice'))

class FilmeForm(ModelForm):
    class Meta:
        model = Filme

def cadastrar(request, filme_id=None):
    filme = None if filme_id is None else (
        get_object_or_404(Filme, id=int(filme_id)))
    if request.method == 'POST':
        CreditosInlineSet = inlineformset_factory(Filme, Credito, extra=3)
        if filme is None:
            form_filme = FilmeForm(request.POST)
        else:
            form_filme = FilmeForm(request.POST, instance=filme)
        if form_filme.is_valid():
            filme = form_filme.save()
            forms_creditos = CreditosInlineSet(request.POST, instance=filme)
            if forms_creditos.is_valid():
                creditos = forms_creditos.save()
                return HttpResponseRedirect(filme.get_absolute_url())

    if filme is None:
        # preparar para criar novo filme  
        form_filme = FilmeForm()
        CreditosInlineSet = inlineformset_factory(Filme, Credito, 
                                                  extra=3, can_delete=False)
        forms_creditos = CreditosInlineSet()
    else:
        # caso contrário, preparar para editar um filme existente
        form_filme = FilmeForm(instance=filme)
        CreditosInlineSet = inlineformset_factory(Filme, Credito, 
                                                  extra=3, can_delete=True)
        forms_creditos = CreditosInlineSet(instance=filme)
    forms = dict(form_filme=form_filme, forms_creditos=forms_creditos)
    return render_to_response('demofilmes/filme_cadastro.html', forms)
