from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, JsonResponse


def cookies_policy(request, template_name='my_portfolio/cookies_policy.html'):
    return render(request, template_name)


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


def experience(request, template_name='my_portfolio/experience.html'):
    lore_ipsum = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed efficitur ex sit amet massa scelerisque scelerisque. Aliquam erat volutpat. Aenean interdum finibus efficitur. Praesent dapibus dolor felis, eu ultrices elit molestie."
    experiences = [("Técnico de mantenimiento", "Saetech SA", "2022 Dic", "Actualidad", lore_ipsum),
                   ("Técnico electronico", "Prexey SA", "9999", "Diciembre 2022", lore_ipsum),
                   ("Oficial electricista", "INGESA", "9999", "9999", lore_ipsum),]
    context = {"experiences": experiences}
    return render(request, template_name, context=context)


def projects(request, template_name='my_portfolio/projects.html'):
    projects = range(10)
    context = {"projects": projects}
    return render(request, template_name, context=context)


def education(request, template_name='my_portfolio/education.html'):
    education = [("Data Scientist", "Abril 2022", "Cursando", "EducacionIT", "loading.png", ["Base de datos", "ETL", "Probabilidad", "Estadistica", "Analisis de datos", "Visualizacion de Datos", "Machine Learning", "Deep Learning", "Optimización de modelos"]),
                 ("JAVA Backend Developer", "Diciembre 2022", "Junio 2023", "Programa ONE - Alura Oracle",
                  "programa_one.png", ["Java", "MySQL", "GIT", "GitHub", "JDBC", "JPA", "API Rest", "Swagger"]),
                 ("Full Stack Web Developer", "Mayo 2022", "Mayo 2023", "EGG Cooperation", "fullstack_web_developer.png", [
                  "Java", "MySQL", "GIT", "GitHub", "JDBC", "JPA", "MVC", "ReactJs"]),
                 ("Reparación de Dispositivos Inteligentes", "Mayo 2019", "Septiembre 2019",
                  "Centro de Formación Profesional 402", "dispositivos_Inteligentes.jpg", ["Electrónica"]),
                 ("Técnico Superior en Automatización y Robótica", "2015", "2017", "UTN - Instituto Nacional de Profesorado Técnico", "tecnicatura_superior.jpeg",
                  ["Análisis Matemático", "Electrónica", "Computación", "Electricidad", "Neumática", "Hidráulica", "Electroneumática", "Automatización", "Robótica", "Seguridad Industrial"]),
                 ("Técnico Electromécanico", "2008", "2014", "Instituto de Educación Técnica Manuel Belgrano", "tecnico_electromecanico.jpg", ["Microsoft Office", "Electricidad", "Carpintería", "Mécanica", "Diseño de planos"])]
    context = {"education": education}
    return render(request, template_name, context=context)

def contact_me(request, template_name='my_portfolio/contact_me.html'):
    return render(request, template_name)
