from django.shortcuts import render, HttpResponse

# Create your views here.

def inicio(request):
    return HttpResponse('Pagina de Inicio')

def historia(request):
    return HttpResponse('Pagina de Historia')

def servicios(request):
    return HttpResponse('Pagina de Servicios')

def visitanos(request):
    return HttpResponse('Pagina de Store')

def contacto(request):
    return HttpResponse('Pagina de Contacto')

def blog(request):
    return HttpResponse('Pagina de Blog')

def prueba(request):
    return HttpResponse('Pagina de Prueba')
