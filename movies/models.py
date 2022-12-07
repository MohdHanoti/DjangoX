from django.db import models
from accounts.models import CustomUser
from django.urls import reverse
# Create your models here.
class Movies(models.Model):
    movie_name=models.CharField(max_length=255, null=False, blank=True)
    purchaser=models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    desc=models.TextField()
    Rank=models.IntegerField()

 
    def str(self):
        return self.movie_name

    def get_absolute_url(self):
        return reverse('movie-list')