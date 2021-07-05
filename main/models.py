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

class Project(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    stack = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(upload_to='uploads/products/')
    link = models.URLField(max_length=500,default='https://github.com/shobhit1215')

    def __str__(self):
        return self.title

class Background(models.Model):
    topic = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    text = models.TextField()
    start = models.CharField(max_length=30)
    end = models.CharField(max_length=30)

    def __str__(self):
        return self.title

class Visitor(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.name



