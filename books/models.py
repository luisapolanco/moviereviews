from django.db import models

from movie.models import Movie

# Create your models here
class Book(models.Model):
    title = models.CharField(max_length=200)
    description =  models.TextField()
    image = models.ImageField(upload_to='books/images/')
    movieUrl = models.ForeignKey(Movie, null = False, blank=False, on_delete=models.CASCADE)    

    def __str__(self):
        return self.title

