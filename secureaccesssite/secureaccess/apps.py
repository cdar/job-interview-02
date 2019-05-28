from django.apps import AppConfig


class SecureaccessConfig(AppConfig):
    name = 'secureaccess'

    def ready(self):
        # noinspection PyUnresolvedReferences
        import secureaccess.signals
