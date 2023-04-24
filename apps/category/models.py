from django.db import models
from django.utils.text import slugify
from django.urls import reverse

# Create your models here.

class Category(models.Model):
    category_name    = models.CharField(max_length=50,unique=True)
    slug             = models.SlugField(max_length=1000, unique=True, blank=True)
    description      = models.TextField(max_length=255,blank=True)
    cat_image        = models.ImageField(upload_to='photos/categories',blank=True)

    

    class Meta:
       db_table             = 'category'
       verbose_name         = 'category'
       verbose_name_plural  = 'categories'

    
    # bu fonksiyon categorilere ait slug değerlerini çekmek için kullanılmaktadır 
    # product_by_category bu kısım url ismi , bu kısım (args=[self.slug]) yönlendirme yapılacak slug değeri
    
    def get_url(self):
        return reverse('products_by_category',args=[self.slug])


    def __str__(self):
        return self.category_name
    

