from django.db import models
from django.contrib import admin
class Vehicle_Details_DB(models.Model):
    company=models.CharField(max_length=10)
    model_n=models.CharField(max_length=10)
    warranty=models.IntegerField()
    mgf_year=models.IntegerField()
    onwed_by=models.CharField(max_length=20)
    locality=models.TextField()
    contact_num=models.CharField(max_length=10,primary_key=True)
    num_plate=models.IntegerField()
class Vehicle_Details_DBAdmin(admin.ModelAdmin):
    list_display=["company","model_n","warranty","mgf_year","onwed_by","locality","contact_num","num_plate"]
# Create your models here.
