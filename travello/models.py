from django.db import models
from embed_video.fields import EmbedVideoField

# Create your models here.

class destination(models.Model):
    
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()
    price =  models.IntegerField() 
    offer = models.BooleanField(default=False)
    link = models.TextField()

    def __str__(self):
        return self.name


    

class destination1(models.Model):
    
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()
    price =  models.IntegerField() 
    offer = models.BooleanField(default=False)
    desc1 = models.TextField()
    desc2 = models.TextField()
    desc3 = models.TextField()
    desc4 = models.TextField()
    desc5 = models.TextField()

    def __str__(self):
        return self.name


class newspage(models.Model):
    
    date = models.IntegerField()
    month = models.CharField(max_length=10)
    img = models.ImageField(upload_to='pics')
    post_title = models.CharField(max_length=100) 
    post_category = models.CharField(max_length=100)
    description = models.TextField()
    link = models.TextField(default='#')

    

class newspost(models.Model):
    
    date = models.IntegerField()
    month = models.CharField(max_length=10)
    img = models.ImageField(upload_to='pics')
    post_title = models.CharField(max_length=100) 
    post_category = models.CharField(max_length=100)
    description = models.TextField()
    link = models.TextField(default='#')



    
class Feedback(models.Model):
    
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    subject = models.CharField(max_length=100)
    message = models.TextField()




class Item(models.Model):
    video = EmbedVideoField()  # same like models.URLField()


class Subscribe(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100) 

    def __str__(self):
        return self.name   
     




 
