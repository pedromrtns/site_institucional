from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import TemplateView, ListView
from .models import Servico
from .forms import ContatoForm

class HomeView(TemplateView):
    template_name = 'app/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['servicos'] = Servico.objects.filter(ativo=True)[:3]
        return context

class SobreView(TemplateView):
    template_name = 'core/sobre.html'

class ServicosView(ListView):
    template_name = 'core/servicos.html'
    model = Servico
    context_object_name = 'servicos'
    queryset = Servico.objects.filter(ativo=True)

def contato(request):
    if request.method == 'POST':
        form = ContatoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Mensagem enviada com sucesso! Em breve entraremos em contato.')
            return redirect('contato')
    else:
        form = ContatoForm()
    
    return render(request, 'core/contato.html', {'form': form}) 