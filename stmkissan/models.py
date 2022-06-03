from distutils.command.upload import upload
from email.mime import image
from email.policy import default
from django.db import models
from  django.utils import timezone
# Create your models here.


class Categorie(models.Model):
    name_cat = models.CharField(max_length=155)
    image_cat = models.ImageField(upload_to = "images/%Y/%m/%d")
    Description = models.TextField()
    date_add = models.DateField(default=timezone.now)

    def __str__(self):
        return self.name_cat




class newCommands(models.Model):
    DUREE_CHOICES = (
        ('un jour', 'un jour '),
        ('2 jour', '2 jour '),
        ('3 jour', '3 jour '),
        ('4 jour', '7 jour '),
        ('Plus ', 'Plus'),
    )
    VILLE_CHOICES = (
        ('casa', 'CasaBlanca'),
    )


    ARGUNCE_CHOICES = (
        ('Intervention urgente', 'Intervention urgente'),
        ('Intervention non urgente', 'Intervention non urgente'),
    )
    client_nom = models.CharField(max_length=55)
    client_prenom = models.CharField(max_length=55)
    email = models.EmailField()
    tel = models.CharField(max_length=13)
    name_command = models.CharField(max_length=255)
    Domain = models.ForeignKey(Categorie , on_delete=models.CASCADE)
    ville = models.CharField(choices=VILLE_CHOICES, default="casa" , max_length=255)
    Description = models.TextField()
    Adreess = models.TextField()
    date_Start = models.DateField()
    argunce = models.CharField(max_length=255 , choices=ARGUNCE_CHOICES)
    Durre_work = models.CharField(max_length=255, choices=DUREE_CHOICES)
    Status = models.BooleanField(default=False)
    image = models.ImageField(default="logo.jpg" , upload_to="ImgField")

    def __str__(self):
        return self.name_command