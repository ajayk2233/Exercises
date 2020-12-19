from django.db import models


class Contacts(models.Model):
    phone1 = models.CharField(max_length=10,null=True,blank=True)
    phone2 = models.CharField(max_length=10,null=True,blank=True)

class School(models.Model):
    gender_choices = (
        ('Male', 'Male'),
        ('Female', 'Female')
    )
    std_choices = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
    )
    name = models.CharField(max_length=30,null=True,blank=True)
    roll_no = models.CharField(max_length=10,null=True,blank=True)
    gender = models.CharField(max_length=6,choices=gender_choices,null=True,blank=True)
    phone = models.ForeignKey(Contacts,on_delete=models.CASCADE,null=True,blank=True)
    std = models.IntegerField(null=True,blank=True,choices=std_choices)
    def __str__(self):
        return(self.name)