from django.shortcuts import render
from django.http import HttpResponse
from cms.models import Pages

# Create your views here.

def nuevonombre(request, uno, dos):
    pag = Pages(name=uno, page=dos)
    pag.save()
    return HttpResponse("Nombre incluido correctamente")

def lista_paginas(request):
    lista_pages = Pages.objects.all()
    respuesta = "<ol>"
    for pages in lista_pages:
        respuesta += '<li><a href= "' + pages.name + '">' + pages.name + '</a>'
    respuesta += "</ol>"
    return HttpResponse(respuesta)

def pages(request, ident):
    try:
        page = Pages.objects.get(name = ident)
        respuesta = page.page
    except Pages.DoesNotExist:
        respuesta = "El nombre no existe. Prueba otra vez."
    return HttpResponse(respuesta)

def mi404(request):
    return HttpResponse("No tenemos lo que nos pides. Prueba otra vez.")
