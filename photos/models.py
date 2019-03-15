from django.db import models
import datetime as dt

# Create your models here.

class Location(models.Model):
    location_name = models.CharField(max_length =30,blank=True)

    def __str__(self):
        return self.location_name

    def save_location(self):
        self.save()    


class Category(models.Model):
    category_name = models.CharField(max_length =30,blank=True)

    def __str__(self):
        return self.category_name

    def save_category(self):
        self.save()




class Image(models.Model):
    image = models.CharField(max_length =30)
    image_name = models.CharField(max_length =30)
    image_description = models.CharField(max_length =30)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.image
    
    def save_editor(self):
        self.save()

    class Meta:
        ordering = ['image']
