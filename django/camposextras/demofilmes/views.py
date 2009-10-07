# coding: utf-8

from django.forms import ModelForm
from django.forms.formsets import formset_factory
from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect

from demofilmes.models import Filme, Credito

class FilmeForm(ModelForm):
    class Meta:
        model = Filme

class CreditoForm(ModelForm):
    class Meta:
        model = Credito

CreditosFormSet = formset_factory(CreditoForm)

def cadastro(request):
    if request.method == 'POST':
        form_filme = FilmeForm(request.POST)
        forms_creditos = CreditosFormSet(request.POST)
        if form_filme.is_valid():
            filme = Filme.objects.create(**form_filme.cleaned_data)
            # TODO: mais um caso em que não consegui usar um reverse...
            return HttpResponseRedirect('/demo/ver/%s/' % filme.id)
    else:
        form_filme = FilmeForm()
        forms_creditos = CreditosFormSet()
    forms = dict(form_filme=form_filme, forms_creditos=forms_creditos)
    return render_to_response('demofilmes/filme_cadastro.html', forms)
