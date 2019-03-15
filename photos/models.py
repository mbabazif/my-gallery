from django.db import models
import datetime as dt

# Create your models here.

class Location(models.Model):
    location_name = models.CharField(max_length =30)

    def __str__(self):
        return self.location_name


class Category(models.Model):
    category_name = models.CharField(max_length =30)

    def __str__(self):
        return self.category_name




class Image(models.Model):
    image = models.CharField(max_length =30)
    image_name = models.CharField(max_length =30)
    image_description = models.CharField(max_length =30)
    location = models.ForeignKey(Location)
    category = models.ForeignKey(Category)

    def __str__(self):
        return self.image
    
    def save_editor(self):
        self.save()

    class Meta:
        ordering = ['image']
