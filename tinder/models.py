from django.db import models
from cloudinary.models import CloudinaryField
from project.constants import interests, drinking , smoking, gender




class User(models.Model):
    class Meta(object):
        db_table = 'user'

    first_name = models.CharField(
        'First Name', max_length=25, blank=False, null=False, db_index=True
    )
    second_name = models.CharField(
        'Second Name', max_length=25, blank=False, null=False, db_index=True
    )
    picture = CloudinaryField(
        'Profile Pic'
    )
    
    gender = models.CharField(
        'Gender', choices=gender, null=False, max_length=100
    )

    age = models.IntegerField(
        'Age', blank=False, null=False, db_index=True
    )
    designation = models.CharField(
        'Designation', max_length=30, blank=False, null=False, db_index=True
    )
    hobbies = models.CharField(
        'Hobbies', max_length=200, blank=False, null=False, db_index=True
    )
    interests = models.CharField(
        'Interested In', choices=interests, null=False, max_length=100
    )
    drinking = models.CharField(
        'Drinking', choices=drinking, null=False, max_length=100
    )
    smoking = models.CharField(
        'Smoking', choices=smoking, null=False, max_length=100
    )
    
    def __str__(self):
        return self.first_name
