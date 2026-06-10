from django.db import models

class Person(models.Model):

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    national_code = models.CharField(
        max_length=10,
        unique=True,
        db_index=True)

    phone_number = models.CharField(max_length=13,unique=True,db_index=True)
    father_name = models.CharField(max_length=100)
    birth_date = models.DateField()
    address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

# Create your models here.
