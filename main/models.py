from django.db import models

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Skill(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    percent = models.IntegerField()

    def __str__(self):
        return self.name

# class Project(models.Model):
#     category = models.ForeignKey(Category,on_delete=models.CASCADE)
#     title = models.CharField(max_length=30)
#     stack = models.CharField(max_length=50)
#     description = models.TextField()
#     image = models.ImageField(upload_to='uploads/products/')

#     def __str__(self):
#         return self.title

