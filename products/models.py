from django.db import models

class KnifekitsItem(models.Model):
    # Product Data
    link = models.URLField(max_length=5000)
    description = models.TextField()
    main_image = models.URLField(max_length=5000)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    sku = models.CharField(max_length=255)
    name = models.CharField(max_length=1000)
    # Flags
    has_discounts = models.BooleanField(default=False)
    has_video = models.BooleanField(default=False)
    has_discounts = models.BooleanField(default=False)
    #SEO / Meta fields
    title = models.CharField(max_length=1000)
    keywords = models.CharField(max_length=255)
    short_desc = models.CharField(max_length=255)
    # stuff
    discounts = models.TextField()
    image_urls = models.TextField()
    breadcrumbs = models.TextField()
    first_crawl = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.sku
