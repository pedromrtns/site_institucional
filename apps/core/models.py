from django.db import models

class Servico(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    icone = models.CharField(max_length=50)
    ordem = models.IntegerField(default=0)
    ativo = models.BooleanField(default=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['ordem']
        verbose_name = 'Serviço'
        verbose_name_plural = 'Serviços'

    def __str__(self):
        return self.titulo

class Contato(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    assunto = models.CharField(max_length=200)
    mensagem = models.TextField()
    criado_em = models.DateTimeField(auto_now_add=True)
    lido = models.BooleanField(default=False)

    class Meta:
        ordering = ['-criado_em']
        verbose_name = 'Contato'
        verbose_name_plural = 'Contatos'

    def __str__(self):
        return f'{self.nome} - {self.assunto}' 