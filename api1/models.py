from django.db import models

# Create your models here.
class Products(models.Model):
    pro_name=models.CharField(max_length=60)
    pro_provider= models.CharField(max_length=60)
    pro_existences= models.PositiveIntegerField()
    pro_date=models.DateField()
    pro_description= models.TextField()
    pro_category= models.CharField(max_length=45)