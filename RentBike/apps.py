from django.apps import AppConfig


class RentBikeConfig(AppConfig):
    name = 'RentBike'

    def ready(self):
        import RentBike.signals
