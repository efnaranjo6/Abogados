from django.db import models

# Create your models here.
class BaseModel(models.Model):
    id = models.AutoField( primary_key= True)
    state = models.BooleanField('Estado', default=True)
    created_date =models.DateField('Fecha de creacion' , auto_now=False , auto_now_add=True)
    modified_date = models.DateTimeField('Fecha de Modificacion', auto_now=True, auto_now_add=False)
    delete_date = models.DateTimeField('Fecha de elimnacion', auto_now=True, auto_now_add=False)

    class Meta:
        abstract =True
        verbose_name="modelo base"
        verbose_name_plural="BaseModels"

  
 