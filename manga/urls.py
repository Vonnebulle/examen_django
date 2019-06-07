from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('Ajouter/Manga', views.manga, name='manga'),
    path('Ajouter/Auteur', views.auteur, name='auteur'),
    path('Liste/Manga', views.liste_manga, name='liste_manga'),
    path('Liste/Auteur', views.liste_auteur, name='liste_auteur'),
    path('le_manga/<int:id>', views.le_manga, name='le_manga'),
    path('suppr_manga/<int:id>', views.suppr_manga, name='suppr_manga'),
]