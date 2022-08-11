from django.db import models

class Products(models.Model):
    title = models.CharField(max_length= 200)
    description = models.CharField(max_length= 2000)
    # image = models.ImageField(upload_to='product_images', null = True, blank = True)

