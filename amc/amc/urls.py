"""amc URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView


urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^projectboard/base.html',  TemplateView.as_view(template_name="projectboard/base.html")),
    url(r'projectboard/', include('projectboard.urls')),
    url(r'controller2.js', TemplateView.as_view(template_name="projectboard/js/controller2.js")),
    url(r'preparation.html',TemplateView.as_view(template_name="projectboard/prep.html")),
    url(r'app.js', TemplateView.as_view(template_name="projectboard/js/app.js")),
    url(r'dashb.js', TemplateView.as_view(template_name="projectboard/js/dashb.js")),
    url(r'projectboard/prep.html', TemplateView.as_view(template_name="projectboard/prep.html")),
    url(r'controller.js', TemplateView.as_view(template_name="projectboard/js/controller.js")),
    url(r'projectboard/project.html', TemplateView.as_view(template_name="projectboard/project.html")),
    url(r'projectboard/dashboard.html', TemplateView.as_view(template_name="projectboard/dashboard.html")),
    url(r'projectboard/help.html', TemplateView.as_view(template_name="projectboard/help.html")),
    url(r'projectboard/about.html', TemplateView.as_view(template_name="projectboard/about.html")),
    url(r'projectboard/features.html', TemplateView.as_view(template_name="projectboard/features.html")),
    url(r'projectboard/project2.html', TemplateView.as_view(template_name="projectboard/project2.html")),
    url(r'preparation.html', TemplateView.as_view(template_name="projectboard/preparation.html"), name="index"),
    url(r'out.json', TemplateView.as_view(template_name="projectboard/out.json"))


]

