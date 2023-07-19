from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, JsonResponse

def index(request, template_name='my_portfolio/index.html'):
    return render(request, template_name)

def sobre_mi(request, template_name='my_portfolio/sobre_mi.html'):
    return render(request, template_name)

def tecnologias(request, template_name='my_portfolio/tecnologias.html'):
    titles = ["Python", "Django", "PowerBI", "SQLite", 
            "JAVA", "Spring", "MySQL", "Bootstrap",
            "GIT", "GitHub", "PostgreSQL", "MongoDB",
            "CSS", "HTML", "Javascript", "ReactJs"]
    images = [f"{nombre.lower()}.svg" for nombre in titles]
    tecnologias = [item for item in zip(titles, images)]
    context = {"tecnologias": tecnologias}
    return render(request, template_name, context=context)