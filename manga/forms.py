from django import forms
from .models import Manga, Auteur


#créer un form à partir d'un Model existant
class MangaForm(forms.ModelForm):
    class Meta:
        model = Manga
        fields = '__all__'
        widgets = {
            'titre': forms.TextInput(attrs={'class': "form-control"}),
            'resumer': forms.Textarea(attrs={'class': "form-control"}),
            'auteur': forms.SelectMultiple(attrs={'class': "form-control"}),

        }


class AuteurForm(forms.ModelForm):
    class Meta:
        model = Auteur
        fields = '__all__'
        widgets = {
            'nom': forms.TextInput(attrs={'class': "form-control"}),
            'prenom': forms.TextInput(attrs={'class': "form-control"}),
            'age': forms.TextInput(attrs={'class': "form-control"}),
            'histoire': forms.Textarea(attrs={'class': "form-control"}),
        }