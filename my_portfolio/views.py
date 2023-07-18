from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, JsonResponse

def index(request, template_name='my_portfolio/index.html'):
    return render(request, template_name)

def sobre_mi(request, template_name='my_portfolio/sobre_mi.html'):
    return render(request, template_name)

def tecnologias(request, template_name='my_portfolio/tecnologias.html'):
    return render(request, template_name)