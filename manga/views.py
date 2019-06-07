from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .forms import MangaForm, AuteurForm
from manga.models import Manga, Auteur


def home(request):
    return render(request, 'home.html')

def manga(request):
    form = MangaForm(request.POST or None, request.FILES or None)
    if form.is_valid(): 
        envoi = True
        form.save()
    return render(request, 'add_manga.html', locals())

def auteur(request):
    form = AuteurForm(request.POST or None)
    if form.is_valid(): 
        envoi = True
        form.save()
    return render(request, 'add_auteur.html', locals())

def liste_auteur(request):
    auteurs = Auteur.objects.all()

    return render(request, 'liste_auteurs.html', {'les_auteurs': auteurs })

def liste_manga(request):
    mangas = Manga.objects.all()
    return render(request, 'liste_mangas.html', {'les_mangas': mangas})

def le_manga(request, id):
    manga = get_object_or_404(Manga, id=id)
    return render(request, 'lemanga.html' ,{'manga':manga})

def suppr_manga(request, id):
    manga = get_object_or_404(Manga, id=id)
    manga.delete()
    return redirect(liste_manga)

def l_auteur(request,id):
    auteur = get_object_or_404(Auteur, id=id)
    return render(request, 'lauteur.html' ,{'auteur':auteur})

def suppr_auteur(request, id):
    auteur = get_object_or_404(Auteur, id=id)
    auteur.delete()
    return redirect(liste_auteur)
