from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User

"""ELIMINAR EN CASCADA : Cuando creamos una clave foranea utilizando esta opcion ,elimina las filas de referencia 
   en la tabla secundaria , cuando la fila referenciada se elimina la tabla primaria que tiene clave primaria.
   
   ACTUALIZAR CASCADA: Cuando creamos una clave externa utilizando ACTUALIZAR CASCADA, las filas de referencia se van
   actualizar en la tabla secundaria cuando la fila referenciada se actualiza en la tabla principal que tiene una clave primaria.
"""


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nombre')
    description = models.TextField(max_length=255, verbose_name='Description')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Creado el')
    
    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
    
    def __str__(self):
        return self.name
    
class Article(models.Model):    
    title = models.CharField(max_length=150, verbose_name='Titulo')
    content = RichTextField(verbose_name='Contenido')
    image = models.ImageField( default='null',verbose_name='Imagen', upload_to="articles")
    public = models.BooleanField(verbose_name='¿Publicado?')
    user = models.ForeignKey(User, editable=False ,verbose_name='Usuario', on_delete=models.CASCADE)
    Categories = models.ManyToManyField(Category,verbose_name='Categorias',  blank=True)
    created_at = models.DateTimeField(auto_now_add=True,verbose_name='Creado el')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Editado el')
    
    class Meta:
        verbose_name = 'Articulo'
        verbose_name_plural = 'Articulos'
        ordering = ['-created_at']
    
        
    def __str__(self):
        return self.title