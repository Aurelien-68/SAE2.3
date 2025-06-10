from django.urls import path
from . import views, avion_views, compagnie_views, vol_views, piste_views, typeavion_views, aeroport_views

urlpatterns = [
    path('', views.base, name='base'),

    # Avion
    path('avion/', avion_views.avion_affiche, name='avion_affiche'),
    path('avion/ajout/', avion_views.avion_ajout, name='avion_ajout'),
    path('avion/update/<int:id>/', avion_views.avion_update, name='avion_update'),
    path('avion/detail/<int:id>/', avion_views.avion_detail, name='avion_detail'),
    path('avion/delete/<int:id>/', avion_views.avion_delete, name='avion_delete'),

    # Compagnie
    path('compagnie/', compagnie_views.compagnie_affiche, name='compagnie_affiche'),
    path('compagnie/ajout/', compagnie_views.compagnie_ajout, name='compagnie_ajout'),
    path('compagnie/update/<int:id>/', compagnie_views.compagnie_update, name='compagnie_update'),
    path('compagnie/detail/<int:id>/', compagnie_views.compagnie_detail, name='compagnie_detail'),
    path('compagnie/delete/<int:id>/', compagnie_views.compagnie_delete, name='compagnie_delete'),

    # Vol
    path('vol/', vol_views.vol_affiche, name='vol_affiche'),
    path('vol/ajout/', vol_views.vol_ajout, name='vol_ajout'),
    path('vol/update/<int:id>/', vol_views.vol_update, name='vol_update'),
    path('vol/detail/<int:id>/', vol_views.vol_detail, name='vol_detail'),
    path('vol/delete/<int:id>/', vol_views.vol_delete, name='vol_delete'),
    path('vol/import/', vol_views.vol_import, name='vol_import'),
    path('vol/fiche/', vol_views.vol_fiche, name='vol_fiche'),

    # Piste
    path('piste/', piste_views.piste_affiche, name='piste_affiche'),
    path('piste/ajout/', piste_views.piste_ajout, name='piste_ajout'),
    path('piste/update/<int:id>/', piste_views.piste_update, name='piste_update'),
    path('piste/detail/<int:id>/', piste_views.piste_detail, name='piste_detail'),
    path('piste/delete/<int:id>/', piste_views.piste_delete, name='piste_delete'),

    # TypeAvion
    path('typeavion/', typeavion_views.typeavion_affiche, name='typeavion_affiche'),
    path('typeavion/ajout/', typeavion_views.typeavion_ajout, name='typeavion_ajout'),
    path('typeavion/update/<int:id>/', typeavion_views.typeavion_update, name='typeavion_update'),
    path('typeavion/detail/<int:id>/', typeavion_views.typeavion_detail, name='typeavion_detail'),
    path('typeavion/delete/<int:id>/', typeavion_views.typeavion_delete, name='typeavion_delete'),

    # Aéroport
    path('aeroport/', aeroport_views.aeroport_affiche, name='aeroport_affiche'),
    path('aeroport/ajout/', aeroport_views.aeroport_ajout, name='aeroport_ajout'),
    path('aeroport/update/<int:id>/', aeroport_views.aeroport_update, name='aeroport_update'),
    path('aeroport/detail/<int:id>/', aeroport_views.aeroport_detail, name='aeroport_detail'),
    path('aeroport/delete/<int:id>/', aeroport_views.aeroport_delete, name='aeroport_delete'),
]
