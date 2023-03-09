from django.db import models

class Logo(models.Model):
    logo_img = models.ImageField(upload_to='logo/')
    
    class Meta:
        verbose_name = 'logo' 
        verbose_name_plural = 'logolar'
    


