# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.utils import timezone

def upload_to(instance,filename):
    timestamp = timezone.now().strftime('%Y%m%d%H%M%S')
    return f'logo/{timestamp}_{filename}'

class ApplicationDisponible(models.Model):
    id = models.BigAutoField(primary_key=True)
    nom = models.CharField(max_length=40, blank=True, null=True)
    logo = models.ImageField(upload_to=upload_to, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'application_disponible'

    def __str__(self):
        chain = f"{self.nom}"
        return chain

    def dico(self):
        return {"id":self.id,"nom": self.nom,"logo":self.logo}


class ApplicationEnCours(models.Model):
    id = models.BigAutoField(primary_key=True)
    id_app = models.ForeignKey(ApplicationDisponible, models.DO_NOTHING, db_column='id_app', blank=True, null=True)
    id_serveur = models.ForeignKey('Serveurs', models.DO_NOTHING, db_column='id_serveur', blank=True, null=True)
    id_utilisateur = models.ForeignKey('Utilisateur', models.DO_NOTHING, db_column='id_utilisateur', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'application_en_cours'

    def __str__(self):
        chain = f"{self.id_app} {self.id_serveur} {self.id_utilisateur}."
        return chain

    def dico(self):
        return {"id_app": self.id_app,"id_serveur":self.id_serveur,"id_utilisateur":self.id_utilisateur}


class Serveurs(models.Model):
    id = models.BigAutoField(primary_key=True)
    nom = models.CharField(max_length=40, blank=True, null=True)
    id_type = models.ForeignKey('TypeServeur', models.DO_NOTHING, db_column='id_type', blank=True, null=True)
    nombre_processeur = models.IntegerField(blank=True, null=True)
    memoire = models.IntegerField(blank=True, null=True)
    stockage = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'serveurs'

    def __str__(self):
        chain = f"{self.nom}"
        return chain

    def dico(self):
        return {"nom": self.nom,"id_type":self.id_type,"nombre_processeur":self.nombre_processeur,"memoire":self.memoire,"stockage":self.stockage}

class ServicesDisponible(models.Model):
    id = models.BigAutoField(primary_key=True)
    nom = models.CharField(max_length=40, blank=True, null=True)
    memoire_necessaire = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'services_disponible'

    def __str__(self):
        chain = f" {self.nom}"
        return chain

    def dico(self):
        return {"nom": self.nom,"memoire_necessaire":self.memoire_necessaire}

class ServicesEnCours(models.Model):
    id = models.BigAutoField(primary_key=True)
    id_service = models.ForeignKey(ServicesDisponible, models.DO_NOTHING, db_column='id_service', blank=True, null=True)
    id_serveur = models.ForeignKey(Serveurs, models.DO_NOTHING, db_column='id_serveur', blank=True, null=True)
    date_lancement = models.DateField(blank=True, null=True)
    memoire_utiliser = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'services_en_cours'


    def __str__(self):
        chain = f"{self.id_service} {self.id_serveur} { self.date_lancement} {self.memoire_utiliser}"
        return chain

    def dico(self):
        return {"id_service": self.id_serveur,"id_serveur":self.id_serveur,"date_lancement":self.date_lancement,"memoire_utiliser":self.memoire_utiliser}

class TypeServeur(models.Model):
    id = models.BigAutoField(primary_key=True)
    type_serveur = models.CharField(max_length=40, blank=True, null=True)
    descript = models.CharField(max_length=300, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'type_serveur'


    def __str__(self):
        chain = f" {self.type_serveur}"
        return chain

    def dico(self):
        return {"type_serveur": self.type_serveur,"descript":self.descript}


class Utilisateur(models.Model):
    id = models.BigAutoField(primary_key=True)
    nom = models.CharField(max_length=30, blank=True, null=True)
    prenom = models.CharField(max_length=30, blank=True, null=True)
    mail = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'utilisateur'


    def __str__(self):
        chain = f"  {self.nom} {self.prenom}"
        return chain

    def dico(self):
        return {"nom": self.nom,"prenom":self.prenom,"mail":self.mail}