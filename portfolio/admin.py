from django.contrib import admin
from .models import Project
# Register your models here.

class ProjectAdmin(admin.ModelAdmin):
    #esta funcion nos permite visualizar solo para lectura los campos de nuestros modelos de fecha de creacion y actualizacion
    #esta funcion se hace debido a que esos campos no se visualizan y esto nos permiten ver ya que django por defecto oculta los campos de fecha
    readonly_fields =('created','updated')

#permite mostrar nuestro proyecto de models para ver en la administracion de proyectos
#poner en el parentesis "ProjectAdmin" permite la funcion extendida
admin.site.register(Project,ProjectAdmin)