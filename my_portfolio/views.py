from django.shortcuts import render
from django.views.generic import FormView, TemplateView
from django.urls import reverse_lazy
from .forms import ContactForm
from . import models
from .auxiliar import all_row_model_to_dict


def cookies_policy(request, template_name='my_portfolio/cookies_policy.html'):
    return render(request, template_name)


def index(request, template_name='my_portfolio/index.html'):
    return render(request, template_name)


def about_me(request, template_name='my_portfolio/about_me.html'):
    return render(request, template_name)

def tecnology(request, template_name='my_portfolio/tecnology.html'):
    tecnologies = all_row_model_to_dict(models.Tecnology)
    context = {"tecnologies": tecnologies}
    return render(request, template_name, context=context)


def experience(request, template_name='my_portfolio/experience.html'):
    experiences = all_row_model_to_dict(models.Experience)
    context = {"experiences": experiences}
    return render(request, template_name, context=context)


def projects(request, template_name='my_portfolio/projects.html'):
    projects = all_row_model_to_dict(models.Project)
    for item in projects:
        item["tags"] = models.Project.objects.get(name=item["name"]).tags.names()
    context = {"projects": projects}
    return render(request, template_name, context=context)


def education(request, template_name='my_portfolio/education.html'):
    education = all_row_model_to_dict(models.Education)
    for item in education:
        item["tags"] = models.Education.objects.get(name=item["name"]).tags.names()
    context = {"education": education}
    return render(request, template_name, context=context)

class ContactView(FormView):
    template_name = 'my_portfolio/contact_me.html'
    form_class = ContactForm
    success_url = reverse_lazy('success')

    def form_valid(self, form):
        form.send()
        return super().form_valid(form)

class ContactSuccessView(TemplateView):
    template_name = 'my_portfolio/success.html'