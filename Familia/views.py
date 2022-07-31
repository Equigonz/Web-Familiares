from django.shortcuts import render

from Familia.models import Familiar

# Create your views here.
def Hola(request):
    return render (request, "miarchivo.html", context={})

def crear_familiar(request):  
    nuevo_familiar = Familiar.objects.create(name = "Paloma Gonzalez", parentezco = "Hija")
    context = {
        "nuevo_familiar": nuevo_familiar
    }
    return render(request,"nuevo_familiar.html", context=context)


def lista_familiar(request):
    familiar = Familiar.objects.all() 
    context = {
        "familiar":familiar
    }    
    return render(request, "lista_familiar.html", context=context)