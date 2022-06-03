from dataclasses import fields
from pyexpat import model
from django import forms
from .models import newCommands , Categorie
from  django.contrib.auth.models import  User


class Commndes(forms.ModelForm):
    date_Start = forms.DateField()
    class Meta:
        model = newCommands
        fields = ('client_nom', 'client_prenom',
                  'email', 'tel', 'name_command', 'Domain', 'ville', 'Description', 'Adreess', 'date_Start', 'argunce', 'Durre_work' , 'image')

class  CategorieForms(forms.ModelForm):
    class Meta:
        model = Categorie
        fields = ('name_cat', 'image_cat', "Description", 'date_add')
