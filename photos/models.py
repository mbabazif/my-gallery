from django.db import models


# Create your models here.

class Location(models.Model):
    location_name = models.CharField(max_length =30,blank=True)

    def __str__(self):
        return self.location_name

    def save_location(self):
        self.save() 

    def delete_location(self):
        '''Method to delete an image from the database'''
        self.delete() 

    def update_location(self):
        '''Method to update an image in the database'''
        self.update()  


class Category(models.Model):
    category_name = models.CharField(max_length =30,blank=True)

    def __str__(self):
        return self.category_name

    def save_category(self):
        '''Method to save the category in the database'''
        self.save()
    
    def delete_category(self):
        '''
        Method to delete the category in the database
        '''
        self.delete()
    
    def update_category(self):
        '''Method to update an image in the database'''
        self.update()


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
    
    @classmethod
    def get_image_by_id(cls, id):
        '''
        Method that loops through the class and pick an anticipated id
        Return:
            selected_image : desired image
        '''
        selected_image = Images.objects.filter_by(id=id)
        return selected_image

    @classmethod
    def search_by_category(cls,search_term):
        photos = cls.objects.filter(category__icontains=search_term)
        return photos


    class Meta:
        ordering = ['image']
