"""
URL configuration for my_portfolio project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cookies-policy', views.cookies_policy, name="cookies-policy"),
    path('', views.index, name="index"),
    path('about_me', views.about_me, name="about_me"),
    path('tecnology', views.tecnology, name="tecnology"),
    path('experience', views.experience, name="experience"),
    path('projects', views.projects, name="projects"),
    path('education', views.education, name="education"),
    path('contact_me', views.ContactView.as_view(), name="contact_me"),
    path('success', views.ContactSuccessView.as_view(), name="success"),
]
