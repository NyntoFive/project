from django.db import models
class Demo(models.Model):
    link = models.URLField(max_length=2000, blank=True, null=True)
    sku = models.CharField(max_length=2000, unique=True)
    name = models.CharField(max_length=2000)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField()
    all_images = models.TextField()
    main_image = models.URLField(max_length=2000)
    breadcrumbs = models.CharField(max_length=2000)
    title = models.CharField(max_length=2000)
    short_desc = models.CharField(max_length=2000)
    keywords = models.CharField(max_length=2000)
    manufacturer = models.CharField(max_length=255, default="")

    def __str__(self):
        return self.sku
    
    