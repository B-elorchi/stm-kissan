from  django.urls import path
from . import views
urlpatterns = [
    path('',  views.home, name="home"),
    path('about/', views.About , name="about"),
    path('contact/', views.contact , name="contact"),
    path('commander/', views.command, name="commander"),
    path('commands/', views.AllCommand, name="commands"),
    path('command/<int:idcmd>/dettails/', views.DettailsCommand, name="dettails"),
    # path('contact/', views.contact, name="contact"),
    path('services/', views.allService, name="services"),
    path('services/<int:idServices>/dettails/', views.serviceDettails, name="servDettails"),
    path('categorie/', views.newCat, name="categorie"),
    path('search/', views.Search, name="search"),
    path('command/<int:id>/delete', views.Delete, name="delete"),
    path('command/<int:id>/valide', views.Valider, name="valide"),
    path('command/<int:id>/nonValide', views.nonValider, name="nvalide"),
]

