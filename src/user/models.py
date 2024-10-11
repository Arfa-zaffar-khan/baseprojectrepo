from django.db import models

class User(models.Model):
    name=models.CharField(max_length=30)
    city=models.CharField(max_length=30)
    email=models.EmailField(max_length=30)
    password=models.CharField(max_length=30)

    class Meta:
        db_table="users"


