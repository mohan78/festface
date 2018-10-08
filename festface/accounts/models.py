from django.db import models
from django.contrib.auth.models import User

class Students(models.Model):
    username = models.ForeignKey(User, related_name="user_student", on_delete=models.CASCADE)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    dob = models.DateField("Date of birth")
    gender = models.CharField(max_length=6)
    phone = models.CharField(max_length=12)
    branch = models.TextField()
    college = models.TextField()
    city = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    pincode = models.CharField(max_length=6)

class Staff(models.Model):
    user = models.ForeignKey(User,related_name="user_staff",on_delete=models.CASCADE)
    is_admin = models.BooleanField()
    can_add_events = models.BooleanField()
    can_read_stats = models.BooleanField()
