from django.apps import AppConfig


class PortfolioConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "portfolio"
    verbose_name='Portafolio' #permite extender el nombre del proyecto como un apodo y tomar ese apodo como nombre principal en el sistema django
    #en settings se invoca su extension de la siguiente forma
