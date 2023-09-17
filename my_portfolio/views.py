from django.shortcuts import render, redirect
from django.views.generic import View, TemplateView
from django.contrib import messages
from .forms import ContactForm
from . import models
from .auxiliar import all_row_model_to_dict, obtain_url_buttons_from_template, get_pages_list
pages_list = get_pages_list()


def cookies_policy(request, template_name='my_portfolio/cookies_policy.html'):
    return render(request, template_name)

def index(request, template_name='my_portfolio/index.html'):
    page_flow = obtain_url_buttons_from_template(models.Pages, template_name)
    context = {"page_flow": page_flow,
               "pages_list": pages_list}
    return render(request, template_name, context=context)

def about_me(request, template_name='my_portfolio/about_me.html'):
    page_flow = obtain_url_buttons_from_template(models.Pages, template_name)
    context = {"page_flow": page_flow,
               "pages_list": pages_list}
    return render(request, template_name, context=context)

def tecnology(request, template_name='my_portfolio/tecnology.html'):
    tecnologies = all_row_model_to_dict(models.Tecnology)
    page_flow = obtain_url_buttons_from_template(models.Pages, template_name)
    context = {"tecnologies": tecnologies,
               "page_flow": page_flow,
               "pages_list": pages_list}
    return render(request, template_name, context=context)

def projects(request, template_name='my_portfolio/projects.html'):
    projects = all_row_model_to_dict(models.Project)
    page_flow = obtain_url_buttons_from_template(models.Pages, template_name)
    for item in projects:
        item["tags"] = models.Project.objects.get(name=item["name"]).tags.names()
    context = {"projects": projects,
               "page_flow": page_flow,
               "pages_list": pages_list}
    return render(request, template_name, context=context)

def education(request, template_name='my_portfolio/education.html'):
    education = all_row_model_to_dict(models.Education)
    page_flow = obtain_url_buttons_from_template(models.Pages, template_name)
    for item in education:
        item["tags"] = models.Education.objects.get(name=item["name"]).tags.names()
    context = {"education": education,
               "page_flow": page_flow,
               "pages_list": pages_list}
    return render(request, template_name, context=context)

def experience(request, template_name='my_portfolio/experience.html'):
    experiences = all_row_model_to_dict(models.Experience)
    page_flow = obtain_url_buttons_from_template(models.Pages, template_name)
    context = {"experiences": experiences,
               "page_flow": page_flow,
               "pages_list": pages_list}
    return render(request, template_name, context=context)

def curriculum(request, template_name='my_portfolio/curriculum.html'):
    curriculums = all_row_model_to_dict(models.Curriculum)
    page_flow = obtain_url_buttons_from_template(models.Pages, template_name)
    context = {"curriculums": curriculums,
               "page_flow": page_flow,
               "pages_list": pages_list}
    return render(request, template_name, context=context)

class ContactView(View):
    template_name = 'my_portfolio/contact.html'
    page_flow = obtain_url_buttons_from_template(models.Pages, template_name)
    success_msg = 'El mensaje se envió correctamente.'
    error_msg = 'Hubo un error al enviar el mensaje.\nIntenta nuevamente, o contactame por otro medio.\nMis redes están abajo. ↓↓↓'

    def get(self, request, *args, **kwargs):
        form = ContactForm()
        context = {'form': form,
                   "page_flow": self.page_flow,
                   "pages_list": pages_list}
        return render(request, self.template_name, context=context)

    def post(self, request, *args, **kwargs):
        form = ContactForm(request.POST)
        try:
            if form.is_valid():
                form.send()
                messages.success(request, self.success_msg)
            else:
                messages.error(request, self.error_msg)
        except:
            messages.error(request, self.error_msg)
        finally:
            return redirect('contact')