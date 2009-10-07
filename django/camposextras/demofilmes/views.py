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

CreditosFormSet = formset_factory(CreditoForm, extra=3)

def cadastro(request):
    if request.method == 'POST':
        form_filme = FilmeForm(request.POST)
        if form_filme.is_valid():
            filme = Filme.objects.create(**form_filme.cleaned_data)
            forms_creditos = CreditosFormSet(request.POST)
            if forms_creditos.is_valid():
                for cred in forms_creditos.cleaned_data:
                    cred['filme'] = filme
                    Credito.objects.create(**cred)
            # TODO: mais um caso em que não consegui usar um reverse...
            return HttpResponseRedirect('/demo/ver/%s/' % filme.id)
    else:
        form_filme = FilmeForm()
        forms_creditos = CreditosFormSet()
    forms = dict(form_filme=form_filme, forms_creditos=forms_creditos)
    return render_to_response('demofilmes/filme_cadastro.html', forms)
