from django.urls import path
from . import views
urlpatterns = [
    path('',views.index, name='index'),
    ###############################################################
    ###################Application#En#Cours########################
    ###############################################################
    path('AppCours/createAC/', views.createAC),
    path('AppCours/confirmationAC/', views.confirmationAC),
    path('AppCours/readAC/<int:id>/',views.readAC),
    path('AppCours/updateAC/<int:id>/',views.updateAC),
    path('AppCours/traitementupdateAC/<int:id>/',views.traitementupdateAC),
    path('AppCours/deleteAC/<int:id>/' ,views.deleteAC),
    ###############################################################
    #######################Application##Disponible#################
    ###############################################################
    path('AppDispo/createAD/', views.createAD),
    path('AppDispo/confirmationAD/', views.confirmationAD),
    path('AppDispo/readAD/<int:id>/', views.readAD),
    path('AppDispo/updateAD/<int:id>/', views.updateAD),
    path('AppDispo/traitementupdateAD/<int:id>/', views.traitementupdateAD),
    path('AppDispo/deleteAD/<int:id>/', views.deleteAD),
    ###############################################################
    #####################Serveur###################################
    ###############################################################
    path('Serveur/createS/', views.createS),
    path('Serveur/confirmationS/', views.confirmationS),
    path('Serveur/readS/<int:id>/', views.readS),
    path('Serveur/updateS/<int:id>/', views.updateS),
    path('Serveur/traitementupdateS/<int:id>/', views.traitementupdateS),
    path('Serveur/deleteS/<int:id>/', views.deleteS),
    path('Serveur/<int:serveur_id>/fiche-pdf/', views.generer_fiche_pdf, name='fiche_pdf'),
    ###############################################################
    #####################Type#Serveur#############################
    ###############################################################
    path('TypeServeur/createTS/', views.createTS),
    path('TypeServeur/confirmationTS/', views.confirmationTS),
    path('TypeServeur/readTS/<int:id>/', views.readTS),
    path('TypeServeur/updateTS/<int:id>/', views.updateTS),
    path('TypeServeur/traitementupdateTS/<int:id>/', views.traitementupdateTS),
    path('TypeServeur/deleteTS/<int:id>/', views.deleteTS),
    ###############################################################
    #####################Service#Cours#############################
    ###############################################################
    path('ServiceCours/createSC/', views.createSC),
    path('ServiceCours/confirmationSC/', views.confirmationSC),
    path('ServiceCours/readSC/<int:id>/', views.readSC),
    path('ServiceCours/updateSC/<int:id>/', views.updateSC),
    path('ServiceCours/traitementupdateSC/<int:id>/', views.traitementupdateSC),
    path('ServiceCours/deleteSC/<int:id>/', views.deleteSC),
    ###############################################################
    #####################Service#Dispo#############################
    ###############################################################
    path('ServiceDispo/createSD/', views.createSD),
    path('ServiceDispo/confirmationSD/', views.confirmationSD),
    path('ServiceDispo/readSD/<int:id>/', views.readSD),
    path('ServiceDispo/updateSD/<int:id>/', views.updateSD),
    path('ServiceDispo/traitementupdateSD/<int:id>/', views.traitementupdateSD),
    path('ServiceDispo/deleteSD/<int:id>/', views.deleteSD),
    ###############################################################
    #####################Utilisateur###############################
    ###############################################################
    path('Utilisateur/createU/', views.createU),
    path('Utilisateur/confirmationU/', views.confirmationU),
    path('Utilisateur/readU/<int:id>/', views.readU),
    path('Utilisateur/updateU/<int:id>/', views.updateU),
    path('Utilisateur/traitementupdateU/<int:id>/', views.traitementupdateU),
    path('Utilisateur/deleteU/<int:id>/', views.deleteU),
]
