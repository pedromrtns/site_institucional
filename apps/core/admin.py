from django.contrib import admin
from .models import Servico, Contato

@admin.register(Servico)
class ServicoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'ordem', 'ativo', 'criado_em', 'atualizado_em')
    list_filter = ('ativo',)
    search_fields = ('titulo', 'descricao')
    ordering = ('ordem',)

@admin.register(Contato)
class ContatoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'assunto', 'criado_em', 'lido')
    list_filter = ('lido',)
    search_fields = ('nome', 'email', 'assunto', 'mensagem')
    ordering = ('-criado_em',)
    readonly_fields = ('criado_em',) 