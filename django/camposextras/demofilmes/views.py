# coding: utf-8

from django.forms import ModelForm
from django.forms.models import modelformset_factory
from django.shortcuts import render_to_response, get_object_or_404
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.views.generic.create_update import delete_object

from demofilmes.models import Filme, Credito

def delete(request, pk):
    return delete_object(request, model=Filme,
                         post_delete_redirect=reverse('demofilmes.indice'))

class FilmeForm(ModelForm):
    class Meta:
        model = Filme

def cadastrar(request, filme_id=None):
    CreditosFormSet = modelformset_factory(Credito, extra=3)
    if filme_id is None:
        filme = None
    else:
        filme = get_object_or_404(Filme, id=int(filme_id))
    if request.method == 'POST':
        if filme is None:
            form_filme = FilmeForm(request.POST)
        else:
            form_filme = FilmeForm(instance=filme)
        if form_filme.is_valid():
            if filme is None:
                filme = form_filme.save()
            else:
                filme = form_filme.save(instance=filme)
            forms_creditos = CreditosFormSet(request.POST)
            if forms_creditos.is_valid():
                for cred in forms_creditos.cleaned_data:
                    if cred: # salva somente os forms preenchidos
                        cred['filme'] = filme                    
                        credito = Credito.objects.get_or_create(**cred)

            return HttpResponseRedirect(filme.get_absolute_url())

    # se o método não é POST...    
    if filme is None:
        # se o film_id é none e o método não é POST...    
        form_filme = FilmeForm()
        forms_creditos = CreditosFormSet(queryset=Credito.objects.none())
    else:
        form_filme = FilmeForm(instance=filme)
        forms_creditos = CreditosFormSet(queryset=filme.credito_set.all())
    forms = dict(form_filme=form_filme, forms_creditos=forms_creditos)
    return render_to_response('demofilmes/filme_cadastro.html', forms)
