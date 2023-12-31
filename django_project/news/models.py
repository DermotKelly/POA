from django.db import models

class News(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='news_images/')
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.title