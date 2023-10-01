from django.apps import AppConfig


class AppGroupConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app_group'

def ready(self):
    import app_group.signals
