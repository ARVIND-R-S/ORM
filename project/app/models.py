from django.db import models
from django.contrib import admin
class Vehicle_Details_DB(models.Model):
    company=models.CharField(max_length=25)
    model=models.CharField(max_length=25)
    showroom=models.CharField(max_length=25)
    myear=models.IntegerField()
    owned_by=models.CharField(max_length=25)
    address=models.TextField()
    register_num=models.CharField(max_length=25,primary_key=True)
    numplate_num=models.IntegerField()
class Vehicle_Details_DBAdmin(admin.ModelAdmin):
    list_display=["company","model","showroom","myear","owned_by","address","register_num","numplate_num"]
# Create your models here.
