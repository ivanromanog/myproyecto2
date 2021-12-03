from django.shortcuts import render
def index(request):
    contexto ={
        "nombre": "Ivan",
        "apellido": "Romano",
        "edad": "37",
        "mascotas": ("Cata", "Sam", "Dawson")

    }
    return render(request, "index.html", contexto)
# Create your views here.
