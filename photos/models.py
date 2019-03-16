from django.db import models


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

    @classmethod
    def search_by_title(cls,search_term):
        photos = cls.objects.filter(title__icontains=search_term)
        return news




class Image(models.Model):
    image = models.CharField(max_length =30)
    image_name = models.CharField(max_length =30)
    image_description = models.CharField(max_length =30)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    p_image = models.ImageField(upload_to = 'images/', blank=True, null=True)
  

    def __str__(self):
        return self.image
    
    def save_image(self):
        '''Method to save an image in the database'''
        self.save()

    def delete_image(self):
        '''Method to delete an image from the database'''
        self.delete()

    def update_image(self):
        '''Method to update an image in the database'''
        self.update()

    
        
    


    class Meta:
        ordering = ['image']
