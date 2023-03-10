from django.db import models

class Logo(models.Model):
    logo_img = models.ImageField(upload_to='logo/')
    logo_url = models.TextField()
    
    class Meta:
        verbose_name = 'logo' 
        verbose_name_plural = 'logolar'
    
class Home_page(models.Model):
    image = models.ImageField(upload_to='slider/')
    title = models.CharField(max_length=100)
    
    class Meta:
        verbose_name = "Bosh sahifa slaydi"
        verbose_name_plural = "Bosh sahifa slaydlari"

