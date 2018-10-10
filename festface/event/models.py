from django.db import models
from accounts.models import Students

class Festmeta(models.Model):
    festname = models.CharField(max_length=300)
    start_date = models.DateField("Start Date")
    end_date = models.DateField("Start Date")
    description = models.TextField()
    venue = models.CharField(max_length=200)
    college = models.CharField(max_length=100)
    branch =  models.TextField()
    college_address = models.TextField()
    city = models.CharField(max_length=200)
    district = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    pincode = models.CharField(max_length=6)
    chief_guest1 = models.CharField(max_length=200,blank=True,null=True)
    chief_guest2 = models.CharField(max_length=200,blank=True,null=True)
    chief_guest3 = models.CharField(max_length=200,blank=True,null=True)
    registration_fee = models.IntegerField(blank=True,null=True)
    accomodation = models.CharField(max_length=1)
    food = models.CharField(max_length=1)
    spocname1 = models.CharField(max_length=200)
    spocname2 = models.CharField(max_length=200,blank=True,null=True)
    spocmail1 = models.CharField(max_length=200)
    spocmail2 = models.CharField(max_length=200,blank=True,null=True)
    spocphone1 = models.CharField(max_length=14)
    spocphone2 = models.CharField(max_length=14,blank=True,null=True)
    festmail = models.CharField(max_length=200)
    collegewebsite = models.CharField(max_length=200)
    username = models.CharField(max_length=100)

    def __str__(self):
        return self.festname

class Events(models.Model):
    festname = models.ForeignKey(Festmeta,on_delete=models.CASCADE,related_name='fest_event')
    title = models.CharField(max_length=200)
    short_desc = models.CharField(max_length=300)
    brief_desc = models.TextField()
    category = models.CharField(max_length=20)
    venue = models.CharField(max_length=100)
    eventdate = models.DateField("Event date")
    registration_fee = models.IntegerField()

    def tell_branch(self):
        return self.category

    def __str__(self):
        return self.title



class Rules(models.Model):
    event = models.ForeignKey(Events, on_delete = models.CASCADE, related_name="event_rules")
    rule = models.TextField()


class Registrations(models.Model):
    festmeta = models.ForeignKey(Festmeta,on_delete=models.CASCADE,related_name="fest_register")
    username = models.ForeignKey(Students,on_delete = models.CASCADE, related_name="user_register")
    event = models.ForeignKey(Events, on_delete = models.CASCADE, related_name="event_register")
    regfeestatus = models.CharField(max_length=3)
