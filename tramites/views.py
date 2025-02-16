from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Tramite
from .forms import TramiteForm
from django.contrib.auth import login
from .forms import RegistroForm

def registro(request):
    if request.method == "POST":
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data["password"])  # Encripta la contraseña
            user.save()
            login(request, user)  # Autentica al usuario después del registro
            return redirect('lista_tramites')  # Redirige después de registrar
    else:
        form = RegistroForm()
    return render(request, 'registration/registro.html', {'form': form})

@login_required
def lista_tramites(request):
    query = request.GET.get('q', '')  # Obtiene el valor del campo de búsqueda
    tramites = Tramite.objects.filter(usuario=request.user)

    if query:
        tramites = tramites.filter(titulo__icontains=query)  # Filtra por título

    return render(request, 'tramites/lista.html', {'tramites': tramites, 'query': query})

@login_required
def crear_tramite(request):
    if request.method == 'POST':
        form = TramiteForm(request.POST)
        if form.is_valid():
            tramite = form.save(commit=False)
            tramite.usuario = request.user
            tramite.save()
            return redirect('lista_tramites')
    else:
        form = TramiteForm()
    return render(request, 'tramites/form.html', {'form': form})

@login_required
def editar_tramite(request, pk):
    tramite = get_object_or_404(Tramite, pk=pk, usuario=request.user)
    if request.method == 'POST':
        form = TramiteForm(request.POST, instance=tramite)
        if form.is_valid():
            form.save()
            return redirect('lista_tramites')
    else:
        form = TramiteForm(instance=tramite)
    return render(request, 'tramites/form.html', {'form': form})

@login_required
def eliminar_tramite(request, pk):
    tramite = get_object_or_404(Tramite, pk=pk, usuario=request.user)
    if request.method == 'POST':
        tramite.delete()
        return redirect('lista_tramites')
    return render(request, 'tramites/eliminar.html', {'tramite': tramite})
