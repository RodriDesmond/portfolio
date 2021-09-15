from django.db import models

# Create your models here.
class BaseModel(models.Model):
    creado = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now_add=True)

    class Meta:
        abstract = True

class Categoria(BaseModel):
    nombre_categoria = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre_categoria

class Jobs(BaseModel):
    categoria = models.ForeignKey(Categoria, related_name='categoria',on_delete=models.CASCADE)
    nombre = models.CharField(max_length=150,null=False)
    valor = models.DecimalField(max_digits=5,decimal_places=2,default=0)

    def __str__(self):
        return self.nombre