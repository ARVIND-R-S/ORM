# Ex02 Django ORM Web Application
## Date: 16.06.2026

## AIM
To develop a Django Application to store and retrieve data from a Vehicle Service Database platform using Object Relational Mapping(ORM).

## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Detect changes and create migration files that describe how to modify the database schema

### STEP 5:
Execute the migration files and update the database schema to match your Django models

### STEP 6:
Create a superuser with full access rights to all models and data through the admin interface.

### STEP 7:
Apply the migration files of the created app to the database

### STEP 8:
Execute Django admin using localhost and create details for 10 entries

## PROGRAM
```
models.py
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

admin.py
from django.contrib import admin
from .models import Vehicle_Details_DB,Vehicle_Details_DBAdmin
admin.site.register(Vehicle_Details_DB,Vehicle_Details_DBAdmin)
# Register your models here.

```


## OUTPUT
![alt text](<Screenshot (14).png>)


## RESULT
Thus the program for creating vehicle service Database using ORM hss been executed successfully.
