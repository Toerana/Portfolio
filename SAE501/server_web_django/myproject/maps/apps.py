from django.apps import AppConfig

class MapsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'maps'


class MapsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'maps'

    def ready(self):
        from .mqtt_client import start_mqtt
        from .mqtt_translator import start_mqtt_translator
        start_mqtt_translator()

        start_mqtt()

