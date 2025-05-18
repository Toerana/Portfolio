from django.shortcuts import render , HttpResponseRedirect
from .models import ApplicationDisponible, ApplicationEnCours, Serveurs, ServicesDisponible, ServicesEnCours, TypeServeur, Utilisateur
from . import models
from .forms import ApplicationDisponibleForm, ApplicationEnCoursForm, ServeursForm, ServicesDisponibleForm, ServicesEnCoursForm, TypeServeurForm, UtilisateurForm
from reportlab.pdfgen import canvas
from django.http import HttpResponse

# Create your views here.

def index(request):
    liste = models.ApplicationDisponible.objects.all()
    liste2 = models.ApplicationEnCours.objects.all()
    liste3 = models.Serveurs.objects.all()
    liste4 = models.ServicesEnCours.objects.all()
    liste5 = models.ServicesDisponible.objects.all()
    liste6 = models.TypeServeur.objects.all()
    liste7 = models.Utilisateur.objects.all()
    return render(request, 'index/index.html', {"liste":liste,"liste2":liste2,"liste3":liste3,"liste4":liste4,"liste5":liste5,"liste6":liste6,"liste7":liste7})


###################################################################
##############APPLICATIO#EN#COURS##################################
###################################################################

def confirmationAC(request):
    lform = ApplicationEnCoursForm(request.POST)
    if lform.is_valid():
        AC = lform.save()
        return HttpResponseRedirect ('/sae/')
    else:
        return render(request,'/sae/createAC.html',{"form": lform})

def createAC(request):
    if request.method == "POST":
        form = ApplicationEnCoursForm(request)
        if form.is_valid():
            AC = form.save()
            return render(request,'AppCours/confirmationAC.html',{"AC" : AC})
        else:
            return render(request,'AppCours/createAC.html',{"form": form})
    else :
        form = ApplicationEnCoursForm()
        return render(request,'AppCours/createAC.html',{"form" : form})

def readAC(request, id):
    AC = models.ApplicationEnCours.objects.get (pk= id)
    return render(request,'AppCours/readAC.html',{"AC": AC})

def updateAC(request,id):
    AC = models.ApplicationEnCours.objects.get(pk=id)
    form = ApplicationEnCoursForm(AC.dico())
    return render(request, "AppCours/createAC.html" ,{"form":form, "id": id})

def traitementupdateAC(request, id):
    lform = ApplicationEnCoursForm(request.POST)
    if lform.is_valid():
        ApplicationEnCours = lform.save(commit=False)
        ApplicationEnCours.id = id;
        ApplicationEnCours.save()
        return HttpResponseRedirect('/sae/')
    else:
        return render(request, 'AppCours/updateAC.html', {"form": lform, "id": id})

def deleteAC(request, id):
    ApplicationEnCours = models.ApplicationEnCours.objects.get(pk=id)
    ApplicationEnCours.delete()
    return HttpResponseRedirect('/sae/')


###################################################################
##############APPLICATION#Dispo####################################
###################################################################


def confirmationAD(request):
    lform = ApplicationDisponibleForm(request.POST)
    if lform.is_valid():
        AD = lform.save()
        return HttpResponseRedirect ('/sae/')
    else:
        return render(request,'/sae/createAD.html',{"form": lform})

def createAD(request):
    if request.method == "POST":
        form = ApplicationDisponibleForm(request.POST,request.FILES)
        if form.is_valid():
            AD = form.save()
            return render(request,'AppDispo/confirmationAD.html',{"AD" : AD})
        else:
            return render(request,'AppDispo/createAD.html',{"form": form})
    else :
        form = ApplicationDisponibleForm()
        return render(request,'AppDispo/createAD.html',{"form" : form})

def readAD(request, id):
    AD = models.ApplicationDisponible.objects.get (pk= id)
    return render(request,'AppDispo/readAD.html',{"AD": AD})

def updateAD(request,id):
    AD = models.ApplicationDisponible.objects.get(pk=id)
    form = ApplicationDisponibleForm(AD.dico())
    return render(request, "AppDispo/createAD.html" ,{"form":form, "id": id})

def traitementupdateAD(request, id):
    lform = ApplicationDisponibleForm(request.POST)
    if lform.is_valid():
        ApplicationDisponible = lform.save(commit=False)
        ApplicationDisponible.id = id;
        ApplicationDisponible.save()
        return HttpResponseRedirect('/sae/')
    else:
        return render(request, 'AppDispo/updateAD.html', {"form": lform, "id": id})

def deleteAD(request, id):
    ApplicationDisponible = models.ApplicationDisponible.objects.get(pk=id)
    ApplicationDisponible.delete()
    return HttpResponseRedirect('/sae/')


###################################################################
##############SERVEUR##############################################
###################################################################



def confirmationS(request):
    lform = ServeursForm(request.POST)
    if lform.is_valid():
        S = lform.save()
        return HttpResponseRedirect ('/sae/')
    else:
        return render(request,'/sae/createS.html',{"form": lform})

def createS(request):
    if request.method == "POST":
        form = ServeursForm(request)
        if form.is_valid():
            S = form.save()
            return render(request,'Serveur/confirmationS.html',{"S" : S})
        else:
            return render(request,'Serveur/createS.html',{"form": form})
    else :
        form = ServeursForm()
        return render(request,'Serveur/createS.html',{"form" : form})

def readS(request, id):
    S = models.Serveurs.objects.get (pk= id)
    return render(request,'Serveur/readS.html',{"S": S})

def updateS(request,id):
    S = models.Serveurs.objects.get(pk=id)
    form = ServeursForm(S.dico())
    return render(request, "Serveur/createS.html" ,{"form":form, "id": id})

def traitementupdateS(request, id):
    lform = ServeursForm(request.POST)
    if lform.is_valid():
        Serveurs = lform.save(commit=False)
        Serveurs.id = id;
        Serveurs.save()
        return HttpResponseRedirect('/sae/')
    else:
        return render(request, 'Serveur/updateS.html', {"form": lform, "id": id})

def deleteS(request, id):
    Serveurs = models.Serveurs.objects.get(pk=id)
    Serveurs.delete()
    return HttpResponseRedirect('/sae/')


###################################################################
##############Type#Serveur#########################################
###################################################################




def confirmationTS(request):
    lform = TypeServeurForm(request.POST)
    if lform.is_valid():
        TS = lform.save()
        return HttpResponseRedirect ('/sae/')
    else:
        return render(request,'/sae/createTS.html',{"form": lform})

def createTS(request):
    if request.method == "POST":
        form = TypeServeurForm(request)
        if form.is_valid():
            TS = form.save()
            return render(request,'TypeServeur/confirmationTS.html',{"TS" : TS})
        else:
            return render(request,'TypeServeur/createTS.html',{"form": form})
    else :
        form = TypeServeurForm()
        return render(request,'TypeServeur/createTS.html',{"form" : form})

def readTS(request, id):
    TS = models.TypeServeur.objects.get (pk= id)
    return render(request,'TypeServeur/readTS.html',{"TS": TS})

def updateTS(request,id):
    TS = models.TypeServeur.objects.get(pk=id)
    form = TypeServeurForm(TS.dico())
    return render(request, "TypeServeur/createTS.html" ,{"form":form, "id": id})

def traitementupdateTS(request, id):
    lform = TypeServeurForm(request.POST)
    if lform.is_valid():
        TypeServeur = lform.save(commit=False)
        TypeServeur.id = id;
        TypeServeur.save()
        return HttpResponseRedirect('/sae/')
    else:
        return render(request, 'TypeServeur/updateTS.html', {"form": lform, "id": id})

def deleteTS(request, id):
    TypeServeur = models.TypeServeur.objects.get(pk=id)
    TypeServeur.delete()
    return HttpResponseRedirect('/sae/')

###################################################################
##############Service#En#Cours#####################################
###################################################################


def confirmationSC(request):
    lform = ServicesEnCoursForm(request.POST)
    if lform.is_valid():
        SC = lform.save()
        return HttpResponseRedirect ('/sae/')
    else:
        return render(request,'ServiceCours/createSC.html',{"form": lform})

def createSC(request):
    if request.method == "POST":
        form = ServicesEnCoursForm(request)
        if form.is_valid():
            SC = form.save()
            return render(request,'ServiceCours/confirmationSC.html',{"SC" : SC})
        else:
            return render(request,'ServiceCours/createSC.html',{"form": form})
    else :
        form = ServicesEnCoursForm()
        return render(request,'ServiceCours/createSC.html',{"form" : form})

def readSC(request, id):
    SC = models.ServicesEnCours.objects.get (pk= id)
    return render(request,'ServiceCours/readSC.html',{"SC": SC})

def updateSC(request,id):
    SC = models.ServicesEnCours.objects.get(pk=id)
    form = ServicesEnCoursForm(SC.dico())
    return render(request, "ServiceCours/createSC.html" ,{"form":form, "id": id})

def traitementupdateSC(request, id):
    lform = ServicesEnCoursForm(request.POST)
    if lform.is_valid():
        ServicesEnCours = lform.save(commit=False)
        ServicesEnCours.id = id;
        ServicesEnCours.save()
        return HttpResponseRedirect('/sae/')
    else:
        return render(request, 'ServiceCours/updateSC.html', {"form": lform, "id": id})

def deleteSC(request, id):
    ServicesEnCours = models.ServicesEnCours.objects.get(pk=id)
    ServicesEnCours.delete()
    return HttpResponseRedirect('/sae/')

###################################################################
##############Service#Disponible###################################
###################################################################

def confirmationSD(request):
    lform = ServicesDisponibleForm(request.POST)
    if lform.is_valid():
        SD = lform.save()
        return HttpResponseRedirect ('/sae/')
    else:
        return render(request,'/sae/createSD.html',{"form": lform})

def createSD(request):
    if request.method == "POST":
        form = ServicesDisponibleForm(request)
        if form.is_valid():
            SD = form.save()
            return render(request,'ServiceDispo/confirmationSD.html',{"SD" : SD})
        else:
            return render(request,'ServiceDispo/createSD.html',{"form": form})
    else :
        form = ServicesDisponibleForm()
        return render(request,'ServiceDispo/createSD.html',{"form" : form})

def readSD(request, id):
    SD = models.ServicesDisponible.objects.get (pk= id)
    return render(request,'ServiceDispo/readSD.html',{"SD": SD})

def updateSD(request,id):
    SD = models.ServicesDisponible.objects.get(pk=id)
    form = ServicesDisponibleForm(SD.dico())
    return render(request, "ServiceDispo/createSD.html" ,{"form":form, "id": id})

def traitementupdateSD(request, id):
    lform = ServicesDisponibleForm(request.POST)
    if lform.is_valid():
        ServicesDisponible = lform.save(commit=False)
        ServicesDisponible.id = id;
        ServicesDisponible.save()
        return HttpResponseRedirect('/sae/')
    else:
        return render(request, 'ServiceDispo/updateSD.html', {"form": lform, "id": id})

def deleteSD(request, id):
    ServicesDisponible = models.ServicesDisponible.objects.get(pk=id)
    ServicesDisponible.delete()
    return HttpResponseRedirect('/sae/')

###################################################################
##############Utilisateur##########################################
###################################################################


def confirmationU(request):
    lform = UtilisateurForm(request.POST)
    if lform.is_valid():
        U = lform.save()
        return HttpResponseRedirect ('/sae/')
    else:
        return render(request,'/sae/createU.html',{"form": lform})

def createU(request):
    if request.method == "POST":
        form = UtilisateurForm(request)
        if form.is_valid():
            U = form.save()
            return render(request,'Utilisateur/confirmationU.html',{"U" : U})
        else:
            return render(request,'Utilisateur/createU.html',{"form": form})
    else :
        form = UtilisateurForm()
        return render(request,'Utilisateur/createU.html',{"form" : form})

def readU(request, id):
    U = models.Utilisateur.objects.get (pk= id)
    return render(request,'Utilisateur/readU.html',{"U": U})

def updateU(request,id):
    U = models.Utilisateur.objects.get(pk=id)
    form = UtilisateurForm(U.dico())
    return render(request, "Utilisateur/createU.html" ,{"form":form, "id": id})

def traitementupdateU(request, id):
    lform = UtilisateurForm(request.POST)
    if lform.is_valid():
        Utilisateur = lform.save(commit=False)
        Utilisateur.id = id;
        Utilisateur.save()
        return HttpResponseRedirect('/sae/')
    else:
        return render(request, 'Utilisateur/updateU.html', {"form": lform, "id": id})

def deleteU(request, id):
    Utilisateur = models.Utilisateur.objects.get(pk=id)
    Utilisateur.delete()
    return HttpResponseRedirect('/sae/')

def generer_fiche_pdf(request, serveur_id):
    # Récupérez les données du serveur et des services en cours
    serveur = Serveurs.objects.get(id=serveur_id)
    services = ServicesEnCours.objects.filter(id_serveur=serveur_id)

    # Créez le fichier PDF
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="fiche_services_serveur_{serveur_id}.pdf"'

    p = canvas.Canvas(response)

    # Dessinez le contenu du PDF
    p.setFont('Helvetica', 12)
    p.drawString(50, 800, f"Serveur: {serveur.nom}")

    y = 750  # Position verticale initiale

    for service in services:
        y -= 20
        p.drawString(50, y, f"Service: {service.id_service.nom}")
        p.drawString(150, y, f"Date de lancement: {service.date_lancement}")
        p.drawString(400, y, f"Mémoire utilisée: {service.memoire_utiliser} Mo")

    p.showPage()
    p.save()

    return response