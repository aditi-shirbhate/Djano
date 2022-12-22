from django.db import models

# Create your models here.

class Blog(models.Model):
    image = models.ImageField(upload_to = 'blog/')
    title = models.CharField(max_length=200)
    price = models.CharField(max_length=200)
    date = models.DateTimeField()
    contact = models.TextField()

    def __str__(self):
        return f"{self.title}-{self.price}-{self.contact}"
    