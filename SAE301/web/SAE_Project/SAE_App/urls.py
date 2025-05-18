# SAE_App/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path("changestate/<int:id>", views.changestate),
    path('login/', views.login_view, name='login_view'),
    path('logout/', views.logout_view, name='logout_view'),
    path('changestate_all/<int:state>', views.changestate_all)
]

