from django.shortcuts import render
from .models import Project



#creamos un archivo views en la carpeta portfolio solo para que pueda
#ser una vista aparte de core exclusivamente de portfolio
def portfolio(request):
    projects = Project.objects.all()
    # {'projects':projects} permite enviar el objeto project directamente al html para poder usarlo en el ciclo for
    return render(request,"portfolio/portfolio.html",{'projects':projects})
