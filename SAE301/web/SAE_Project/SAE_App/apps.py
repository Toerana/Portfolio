# webapp/apps.py

from django.apps import AppConfig
from django.contrib.auth import get_user_model

class SAE_AppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'SAE_App'

    def ready(self):
        # Change the username from 'admin' to something else
        User = get_user_model()
        admin_user = User.objects.filter(username='admin').first()

        if admin_user:
            admin_user.username = 'admin'
            admin_user.save()
        else:
            User.objects.create_user(username='admin', password='toto')
