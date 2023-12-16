from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse 

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Post(models.Model): 
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_updated = models.DateTimeField(auto_now_add=True)
    categories = models.ManyToManyField(Category)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self): 
        return reverse('post-detail', kwargs={'pk': self.pk}) 



class Slider(models.Model):
    title = models.CharField(max_length=200, blank=False)
    description = models.TextField(max_length=800, blank=False)
    image = models.ImageField(upload_to='slider/',blank=False)

    def __str__(self):
        return self.title
    

    

    