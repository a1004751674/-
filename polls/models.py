from django.db import models

# Create your models here.
# class Newsdata(models.Model):
#     title = models.CharField(blank=True, null=True, max_length=50)
#     media = models.CharField(blank=True, null=True, max_length=10)
#     time = models.CharField(blank=True, null=True, max_length=20)
#     content = models.CharField(blank=True, null=True,max_length=1000)
#     def __str__(self):
#         return self.title
    
class Newsdata(models.Model):
    media = models.CharField(blank=True, null=True, max_length=10)
    title = models.CharField(blank=True, null=True, max_length=50)
    media = models.CharField(blank=True, null=True, max_length=10)
    time = models.CharField(blank=True, null=True, max_length=20)
    content = models.CharField(blank=True, null=True,max_length=1000)
    MediaScr = models.CharField(blank=True, null=True,max_length=1000)
    def __str__(self):
        return self.title    

class frequencytitle(models.Model):
    word = models.CharField(blank=True, null=True, max_length=50)
    frequency = models.IntegerField(blank=True, null=True)
    def __str__(self):
        return self.word
    
class frequencycontent(models.Model):
    word = models.CharField(blank=True, null=True, max_length=50)
    frequency = models.IntegerField(blank=True, null=True)
    def __str__(self):
        return self.word