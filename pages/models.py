from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Page(models.Model): #entidad
     title = models.CharField(max_length=50, verbose_name="Titulo")
     content =RichTextField(verbose_name="contenido")
     slug =models.CharField(unique=True,max_length=150, verbose_name="URL amigable")
     public =models.BooleanField(verbose_name="¿visible?")
     order =models.IntegerField(default=0,verbose_name="Order")
     created_at =models.DateTimeField(auto_now_add=True, verbose_name="Creación:")
     update_at =models.DateTimeField(auto_now_add=True, verbose_name="Actualizacion:")
     
     class Meta:
        verbose_name= "Página"
        verbose_name_plural= "Páginas"
     
     def __str__(self):
        return self.title
         