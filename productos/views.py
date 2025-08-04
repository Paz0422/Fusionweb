from django.shortcuts import render

# Create your views here.

def productos(request):
    """
    Esta vista se encarga de mostrar la página de productos.
    """
    # Aquí podrías agregar lógica para obtener productos de la base de datos
    context = {} 
    return render(request, 'productos/productos.html', context)