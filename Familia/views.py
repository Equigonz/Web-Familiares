from http.client import HTTPResponse
from django.shortcuts import render, redirect
from Familia.models import Familiar
from Familia.forms import Formulario_familia

# Create your views here.
def Hola(request):
    return render (request, "miarchivo.html", context={})

def crear_familiar(request):  
    
    if request.method == "POST":
           
       form = Formulario_familia(request.POST)

       if form.is_valid():
           Familiar.objects.create(
            name = form.cleaned_data["name"],
            parentezco = form.cleaned_data["parentezco"]
           )
           return redirect(lista_familiar)
          
    elif request.method == "GET":
             form = Formulario_familia()
             context = {"form": form}
             return render(request,"nuevo_familiar.html", context=context)


def lista_familiar(request):
    familiar = Familiar.objects.all() 
    context = {
        "familiar":familiar
    }    
    return render(request, "lista_familiar.html", context=context)

def primer_formulario(request):
    print(request.method)
    if request.method == "POST":
        print(request.POST)
    return render(request, "primer_formulario.html", context={})    

def search_familiar(request):
    print(request.GET)
    return HTTPResponse(request.GET)