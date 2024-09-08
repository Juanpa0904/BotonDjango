from django.shortcuts import render
from django.http import HttpResponse

def mostrar_mensaje(request):
    if request.method == 'POST':
        return HttpResponse('xxxTU COMPUTADORA HA SIDO INVADIDAxxx')
    return render(request, 'mi_app/boton.html')
