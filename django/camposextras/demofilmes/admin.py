# coding: utf-8

from django.contrib import admin
from demofilmes.models import Filme, Credito

class CreditoInline(admin.TabularInline):
    model = Credito

class FilmeAdmin(admin.ModelAdmin):
    inlines = [CreditoInline]

admin.site.register(Filme, FilmeAdmin)
