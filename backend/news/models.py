from django.db import models

# Create your models here.
class New(models.Model):
    image = models.ImageField(upload_to='news/')
    title = models.CharField(max_length=255)
    description = models.TextField()


    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title