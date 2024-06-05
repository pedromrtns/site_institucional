from django.shortcuts import render, redirect
from django.contrib import messages

def home(request):
    return render(request, "app/home.html")

def recursos(request):
    return render(request, 'app/recursos.html')

def contato(request):
    if request.method == "POST":
        email = request.POST.get('email')
        message = request.POST.get('message')
        messages.success(request, 'Sua mensagem foi enviada com sucesso!')

        return redirect('home')
    
    return redirect('home')

def sobre_nos(request):
    return render(request, 'app/sobre_nos.html')

def servicos(request):
    return render(request, 'app/servicos.html')
