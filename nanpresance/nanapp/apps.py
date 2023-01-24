from django.apps import AppConfig


class NanappConfig(AppConfig):
    name = 'nanapp'
    # new code for call apscheduler
    def ready(self):
        from .autotast import updateqrcode
        updateqrcode.start()