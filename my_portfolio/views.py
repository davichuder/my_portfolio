from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, JsonResponse

def index(request, template_name='my_portfolio/index.html'):
    return render(request, template_name)

def about_me(request, template_name='my_portfolio/about_me.html'):
    return render(request, template_name)

def tecnology(request, template_name='my_portfolio/tecnology.html'):
    titles = ["Python", "Django", "PowerBI", "SQLite", 
            "JAVA", "Spring", "MySQL", "Bootstrap",
            "GIT", "GitHub", "PostgreSQL", "MongoDB",
            "CSS", "HTML", "Javascript", "ReactJs"]
    images = [f"{tittle.lower()}.svg" for tittle in titles]
    tecnologies = [item for item in zip(titles, images)]
    context = {"tecnologies": tecnologies}
    return render(request, template_name, context=context)

def education(request, template_name='my_portfolio/education.html'):
    return render(request, template_name)