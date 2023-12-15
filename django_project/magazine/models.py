from django.db import models

class Magazine(models.Model):
    title = models.CharField(max_length=255)
    cover_image = models.ImageField(upload_to='covers/')
    pdf_file = models.FileField(upload_to='magazines/')
    publication_date = models.DateField()
    description = models.TextField()

    def __str__(self):
        return self.title
