from django.db import models

# Create your models here.
class Threads(models.Model):
    threadID =  models.IntegerField(default=000, primary_key = True)
    threadName = models.CharField(max_length=200)
    red = models.IntegerField(default=000)
    green = models.IntegerField(default=000)
    blue = models.IntegerField(default=000)
    threadHex =  models.CharField(max_length=200)


    def __str__(self):              # __unicode__ on Python 2
        return self.threadName
