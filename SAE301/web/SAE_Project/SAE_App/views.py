# views.py

from django.shortcuts import render, redirect
from .models import Values
from .forms import LoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import paho.mqtt.publish as publish



topic = 'SAE31/Home'
brocker_address = '192.168.228.192'
#TODO voir le brocker
from django.shortcuts import render, HttpResponseRedirect
from .models import Values
# Create your views here.





    

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                return render(request, 'SAE_App/login.html', {'form': form, 'error_message': 'Invalid credentials'})
    else:
        form = LoginForm()

    return render(request, 'SAE_App/login.html', {'form': form})

@login_required
def logout_view(request):
    logout(request)
    return redirect('login_view')

def envoiMqtt(message):
    try:
        publish.single(topic, message, hostname= brocker_address)
        print(f"Message '{message}' sent to MQTT topic '{topic}' successfully.")
    except Exception as e:
        print(f"Failed to send message to MQTT topic '{topic}': {e}")    


def changestate(request, id):
    prise = Values.objects.get(pk=id)
    prise.toggle_state()
    if prise.etat:
        etat = 1
    elif not prise.etat:
        etat = 0
    message = f"prise:{prise.prise}/state:{etat}"
    print(message)
    envoiMqtt(message)
    return HttpResponseRedirect('/SAE_App/home')

def changestate_all(request, state):
    liste = list(Values.objects.all())
    if state == 0:
        for prise in liste:
            etat = 0
            prise.all_off()
            message = f"prise:{prise.prise}/state:{etat}"
            print(message)
            envoiMqtt(message)
    elif state == 1:
        for prise in liste:
            etat = 1
            prise.all_on()
            message = f"prise:{prise.prise}/state:{etat}"
            print(message)
            envoiMqtt(message)
    return HttpResponseRedirect('/SAE_App/home')

    
@login_required  
def home(request):
    values_list = Values.objects.all()
    context = {'values_list': values_list}
    return render(request, 'SAE_App/home.html', context)