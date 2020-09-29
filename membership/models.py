import random
from django.db import models

def genrate_no():
        return(random.randint(1000000000,9999999999))

class info(models.Model):
    f_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    photo_main = models.ImageField(upload_to="sena_members")
    ward_no = models.IntegerField()
    location = models.TextField()
    assembly = models.CharField(max_length=50)
    contact = models.PositiveIntegerField()
    email = models.EmailField()
    dob = models.DateField()
    post = models.CharField(max_length=100)
    tenure1 = models.PositiveIntegerField()
    tenure2 = models.IntegerField( default='Till-Now')
    position = models.CharField(max_length=250)
    blood_g = models.CharField(max_length=20)
    education = models.CharField(max_length=200)
    pyear = models.IntegerField()
    occupation = models.CharField(max_length=220)
    uidai = models.IntegerField()
    id_number = models.IntegerField(default=genrate_no(),unique=True)


    def __str__(self):
        return f'{self.f_name}info'

