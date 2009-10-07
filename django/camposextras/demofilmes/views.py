# coding: utf-8

from django.forms import ModelForm
from django.forms.formsets import formset_factory
from django.shortcuts import render_to_response, get_object_or_404
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect

from demofilmes.models import Filme, Credito

# usei dois ModelForms, mas apenas para economizar digitação aqui, porque
# o objetivo deste exemplo é lidar com Forms de qualquer tipo, por isso a
# view não usa o método save dos forms.

class FilmeForm(ModelForm):
    class Meta:
        model = Filme

class CreditoForm(ModelForm):
    class Meta:
        model = Credito

CreditosFormSet = formset_factory(CreditoForm, extra=3)

def dict_from_instance(instance):
    ''' builds a dict from the fields of a model instance '''
    return dict( (field.name, getattr(instance, field.name)) 
                        for field in instance._meta.fields )

def cadastrar(request, filme_id=None):
    if filme_id is not None:
        filme = get_object_or_404(Filme, id=filme_id)
    if request.method == 'POST':
        form_filme = FilmeForm(request.POST)
        if form_filme.is_valid():
            if filme_id is None:
                filme = Filme.objects.create(**form_filme.cleaned_data)
            forms_creditos = CreditosFormSet(request.POST)
            if forms_creditos.is_valid():
                for cred in forms_creditos.cleaned_data:
                    if not cred: continue # skip empty subforms
                    cred['filme'] = filme
                    Credito.objects.get_or_create(**cred)
            # TODO: mais um caso em que não consegui usar um reverse...
            return HttpResponseRedirect('/demo/ver/%s/' % filme.id)
    else:
        if filme_id is None:
            form_filme = FilmeForm()
            forms_creditos = CreditosFormSet()
        else:
            form_filme = FilmeForm(initial=dict_from_instance(filme))
            creditos = [dict_from_instance(c) for c in filme.credito_set.all()]
            forms_creditos = CreditosFormSet(initial=creditos)            
    forms = dict(form_filme=form_filme, forms_creditos=forms_creditos)
    return render_to_response('demofilmes/filme_cadastro.html', forms)
