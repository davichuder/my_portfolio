from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, JsonResponse

def index(request, template_name='my_portfolio/index.html'):
    return render(request, template_name)

def about_me(request, template_name='my_portfolio/about_me.html'):
    return render(request, template_name)

def tecnology(request, template_name='my_portfolio/tecnology.html'):
    titles = ["Python", "Django", "PowerBI", "SQLite", 
            "Java", "Spring", "MySQL", "Bootstrap",
            "GIT", "GitHub", "PostgreSQL", "MongoDB",
            "CSS", "HTML", "Javascript", "ReactJs"]
    images = [f"{tittle.lower()}.svg" for tittle in titles]
    tecnologies = [item for item in zip(titles, images)]
    context = {"tecnologies": tecnologies}
    return render(request, template_name, context=context)

def education(request, template_name='my_portfolio/education.html'):
    education = [("Data Scientist", "Abril 2022", "Cursando", "EducacionIT", "img.webp", ["Base de datos", "ETL", "Probabilidad", "Estadistica", "Analisis de datos", "Visualizacion de Datos", "Machine Learning", "Deep Learning", "Optimización de modelos"]),
    ("JAVA Backend Developer", "Diciembre 2022", "Junio 2023", "Programa ONE - Alura Oracle", "img.webp", ["Java", "MySQL", "GIT", "GitHub", "JDBC", "JPA", "API Rest", "Swagger"]),
    ("Full Stack Web Developer", "Mayo 2022", "Mayo 2023", "EGG Cooperation", "img.webp", ["Java", "MySQL", "GIT", "GitHub", "JDBC", "JPA", "MVC", "ReactJs"]),
    ("Técnico Superior en Automatización y Robótica", "2015", "2017", "UTN - Instituto Nacional de Profesorado Técnico", "cv.png"),
    ("Técnico Electromécanico", "2008", "2014", "Instituto de Educación Técnica Manuel Belgrano", "cv.png")]
    context = {"education": education}
    return render(request, template_name, context=context)