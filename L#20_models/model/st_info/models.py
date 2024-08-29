from django.db import models

# Create your models here.
class student(models.Model):
    st_id=models.IntegerField()
    st_name=models.CharField(max_length=50)
    st_email=models.EmailField( max_length=50)
    st_pass=models.CharField(max_length=50)