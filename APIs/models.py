from django.db import models

# Create your models here.
# class Calc(models.Model):
#     title = models.CharField(max_length=200)
#     body = models.TextField()
#     rate = models.FloatField()
#     count = models.IntegerField()
class Video(models.Model):
    # _id = models.IntegerField() 
    word = models.TextField()
    url = models.TextField()
    class Meta:
        db_table = "APIs_video"