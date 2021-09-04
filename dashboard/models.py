from django.db import models


class Storage(models.Model):
    date_time=models.DateTimeField(null=True,blank=True)
    link=models.URLField(null=True,blank=True,max_length=400)
    name = models.CharField(null=True,blank=True,max_length=400)
    key=models.CharField(unique=True,null=True,blank=True,max_length=400)
    converted_link=models.URLField(null=True,blank=True,max_length=400)
    count=models.IntegerField(null=True,blank=True,default=0)

