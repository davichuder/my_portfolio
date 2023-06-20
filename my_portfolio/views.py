from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, JsonResponse

def index(request, template_name='my_portfolio/index.html'):
    return render(request, template_name)