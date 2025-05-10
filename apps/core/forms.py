from django import forms
from .models import Contato

class ContatoForm(forms.ModelForm):
    class Meta:
        model = Contato
        fields = ['nome', 'email', 'assunto', 'mensagem']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Seu nome'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'seu@email.com'}),
            'assunto': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Assunto da mensagem'}),
            'mensagem': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Sua mensagem'}),
        } 