from django.http import  HttpResponse

def lista_inventario(request):
    inventario = Inventario.objects.all()
    return render(request, 'inventario.html', {'inventario': inventario})