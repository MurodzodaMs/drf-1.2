from django.apps import AppConfig


class AccoutnsConfig(AppConfig):
    name = 'accoutns'

    def ready(self):
        import accoutns.signals