from django.shortcuts import render, redirect
from .forms import LoginForm
from django.contrib.auth import authenticate, login




def login_view(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('kullanici_adi')
        password = form.cleaned_data.get('sifre')
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect('form1_view')
    return render(request, 'kullanicigiris.html', {'form': form})
