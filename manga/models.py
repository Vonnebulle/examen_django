from django.db import models
from django.utils import timezone

class Auteur(models.Model):
    nom = models.CharField(max_length=30)
    prenom = models.CharField(max_length=30)
    age = models.IntegerField()
    histoire = models.TextField(null=True)

    

    def __str__(self):
        return self.nom

class Manga(models.Model):
    titre = models.CharField(max_length=100)
    resumer = models.TextField(null=True)
    auteur = models.ManyToManyField(Auteur, related_name="mangas")
    image = models.ImageField()
    def __str__(self):
        return self.titre

