from django.shortcuts import render, get_object_or_404, redirect
from .models import Libro
from .forms import LibroForm

def listar(request):
    libros = Libro.objects.all()
    return render(request, 'libros/listar_libros.html', {'libros': libros})

def crear(request):
    if request.method == 'POST':
        form = LibroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('libros:listar')
    else:
        form = LibroForm()
    return render(request, 'libros/formulario_libro.html', {'form': form, 'accion': 'Crear'})

def editar(request, id):
    libro = get_object_or_404(Libro, id=id)
    if request.method == 'POST':
        form = LibroForm(request.POST, instance=libro)
        if form.is_valid():
            form.save()
            return redirect('libros:listar')
    else:
        form = LibroForm(instance=libro)
    return render(request, 'libros/formulario_libro.html', {'form': form, 'accion': 'Editar'})

def eliminar(request, id):
    libro = get_object_or_404(Libro, id=id)
    if request.method == 'POST':
        libro.delete()
        return redirect('libros:listar')
    return render(request, 'libros/confirmar_eliminacion.html', {'libro': libro})