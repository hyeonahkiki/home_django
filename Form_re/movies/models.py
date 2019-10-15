from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=100)
    audience = models.IntegerField()
    open_date = models.DateField()

class Comment(models.Model):
    content = models.CharField(max_length=100)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)