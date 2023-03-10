from django.db import models

class Logo(models.Model):
    logo_img = models.ImageField(upload_to='logo/')
    logo_url = models.TextField()
    
    class Meta:
        verbose_name = 'logo' 
        verbose_name_plural = 'logolar'
    
class Home_page(models.Model):
    image = models.ImageField(upload_to='slider/')
    img_url = models.TextField()
    title = models.CharField(max_length=100)
    
    class Meta:
        verbose_name = "Bosh sahifa slaydi"
        verbose_name_plural = "Bosh sahifa slaydlari"

class Category(models.Model):
    category_name = models.CharField(max_length=100)
    
    class Meta:
        verbose_name = "Kategoriya"
        verbose_name_plural = "Kategoriyalar"
    def __str__(self):
        return self.category_name

class Album(models.Model):
    title = models.CharField(("Albom nomi:"), max_length=50)
    category = models.ForeignKey("Category", verbose_name=("Kategoriyani tanlang:"), on_delete=models.CASCADE)
    img = models.TextField()
    
    class Meta:
        verbose_name = "Albom"
        verbose_name_plural = "Albomlar"