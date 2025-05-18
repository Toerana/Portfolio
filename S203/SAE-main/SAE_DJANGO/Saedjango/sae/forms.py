from django import forms
from .models import ApplicationDisponible, ApplicationEnCours, Serveurs, ServicesDisponible, ServicesEnCours, TypeServeur, Utilisateur

class ApplicationDisponibleForm(forms.ModelForm):
    class Meta:
        model = ApplicationDisponible
        fields = '__all__'

class ApplicationEnCoursForm(forms.ModelForm):
    class Meta:
        model = ApplicationEnCours
        fields = '__all__'

class ServeursForm(forms.ModelForm):
    class Meta:
        model = Serveurs
        fields = '__all__'

class ServicesDisponibleForm(forms.ModelForm):
    class Meta:
        model = ServicesDisponible
        fields = '__all__'

class ServicesEnCoursForm(forms.ModelForm):
    class Meta:
        model = ServicesEnCours
        fields = '__all__'

class TypeServeurForm(forms.ModelForm):
    class Meta:
        model = TypeServeur
        fields = '__all__'

class UtilisateurForm(forms.ModelForm):
    class Meta:
        model = Utilisateur
        fields = '__all__'