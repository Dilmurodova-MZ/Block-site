from django.db import models
from django.urls import reverse
import uuid

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
        
    
class Blog(models.Model):
    title = models.CharField(max_length=150)
    short_title = models.TextField()
    content = models.TextField()
    date  = models.DateField()
    img_url = models.TextField()
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=False)
    
    class Meta:
        verbose_name = "Blog"
        verbose_name_plural = "Bloglar"
        
    def get_absolute_url(self):
        return reverse("blog", kwargs={"post_id": self.pk})
    
class Gallery(models.Model):
    img_url = models.TextField()
    
    class Meta():
        verbose_name = "Gallereya"
        verbose_name_plural = "Gallereyalar"