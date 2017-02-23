"""
url(r'projectboard/base.html', TemplateView.as_view(template_name="projectboard/base.html")),
    url(r'controller2.js', TemplateView.as_view(template_name="projectboard/js/controller2.js")),
    url(r'app.js', TemplateView.as_view(template_name="projectboard/js/app.js")),
    url(r'app.js', TemplateView.as_view(template_name="projectboard/dashn.html")),

    url(r'dashb.js', TemplateView.as_view(template_name="projectboard/js/dashb.js")),
    url(r'controller.js', TemplateView.as_view(template_name="projectboard/js/controller.js")),
    url(r'projectboard/project.html', TemplateView.as_view(template_name="projectboard/project.html")),
    url(r'projectboard/dashboard.html', TemplateView.as_view(template_name="projectboard/dashboard.html")),
    url(r'projectboard/help.html', TemplateView.as_view(template_name="projectboard/help.html")),
    url(r'projectboard/about.html', TemplateView.as_view(template_name="projectboard/about.html")),
    url(r'projectboard/features.html', TemplateView.as_view(template_name="projectboard/features.html")),
    url(r'projectboard/project2.html', TemplateView.as_view(template_name="projectboard/project2.html")),

    url(r'preparation.html', TemplateView.as_view(template_name="projectboard/preparation.html"), name="index"),
"""



from django.views.generic import TemplateView

from django.conf.urls import url, include

from . import views

urlpatterns = [

    url(r'^prep_ke_baad.html$', views.index,name='index'),
    url(r'^disp.html$', views.index2, name='index2'),
    url(r'^modify$',views.modify, name='modify'),
    url(r'^markit$', views.markit, name='markit'),
    url(r'^markit2$', views.markit2, name='markit2'),
    url(r'^random$', views.random, name='random'),
    url(r'create_post', views.create_post, name='create_post'),
    url(r'^view$', views.view, name='view')
    ]