from django.db import models

# Create your models here.
class Project(models.Model):
   # objects = ["--errors-only","--load-plugins","pylint_django",]
    objects = [
        "--errors-only",
        "--load-plugins",
        "pylint_django"
    ]
    title=models.CharField(verbose_name="Titulo") #CharField seria una cadena corta de caracteres
    description=models.TextField(verbose_name="Descripcion") #TextField seria una cadena larga de caracteres
    image=models.ImageField(verbose_name="Imagen",upload_to="projects") #ImageFields seria tipo imagenes
    #upload_to="projects"=los archivos subidos se almacenarán en un subdirectorio llamado "projects" dentro del directorio de medios.
    created=models.DateTimeField(auto_now_add=True,verbose_name="Fecha de creacion") #DateTimeField seria una variable que almacena
    # la fecha en que se crea los datos, en este caso "auto_now_add" almacena en el momento en que se creo o "añadio" a la base
    updated=models.DateTimeField(auto_now=True,verbose_name="Fecha de actualizacion") #almacena en el momento que se actualiza la variable cuando se modifica
    link = models.URLField(verbose_name="Direccion web",null=True,blank=True)
   #---------Espacio explicando el model link---------------------
   #null=True: Esto significa que en la base de datos,
   # este campo puede almacenar valores nulos. Es decir,
   # un registro en la base de datos puede tener un valor
   # nulo para este campo.
    #blank=True: Esto se aplica a la validación en los
   # formularios. Si blank está establecido en True, el campo
   # no es obligatorio en los formularios. En otras palabras,
   # cuando se crea un formulario basado en este modelo,
   # el campo puede estar vacío y aún así se considerará válido.

   #está diseñado para almacenar URLs. Además, se permite que este
   # campo tenga valores nulos en la base de datos, y no es obligatorio
   # en los formularios.




    class Meta:
        verbose_name="proyecto"
        verbose_name_plural="proyectos"
        #estos verbose_name permite generar los apodos en singular y plural en caso de que haya un solo proyecto o mas
        ordering =["-created"]
        #permite mostrar los proyectos de orden descendente, osea el que fue primero creado y para abajo los proyectos posteriores, por eso esta el signo de menos -
        #en caso de no poner el signo - se mostraria el proyecto mas reciente y en ultimo el primer proyecto creado

    def __str__(self):
        return self.title #permite devolver el nombre del proyecto en el sistema portafolio
        #para no ver solamente "project object" sino ver su nombre verdadero