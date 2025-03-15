from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='products/')
    file = models.URLField()
    technical_specification = models.ForeignKey('technical_specification',on_delete=models.CASCADE)
    category = models.ForeignKey('CategoryModel',on_delete=models.CASCADE)




class technical_specification(models.Model):
    max_weight = models.CharField(max_length=100)
    cargo_capacity = models.CharField(max_length=100)
    dimensions = models.CharField(max_length=100)
    wheelbase = models.CharField(max_length=100)
    wheel_formula = models.CharField(max_length=100)
    engine_volume = models.CharField(max_length=100)
    max_power = models.CharField(max_length=100)
    fuel_type= models.CharField(max_length=100)



class CategoryModel(models.Model):
    title = models.CharField(max_length=255)
    img = models.ImageField(upload_to='category/')


    def __str__(self):
        return self.title