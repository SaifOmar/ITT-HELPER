from django.db import models
# Create your models here.
# note make models for courses /career paths/events/...
# many to many relations 
from django.db import models
from django.conf import settings
from datetime import datetime
from django.utils.timezone import now

class FirstSteps(models.Model):
    first_steps = models.CharField(max_length=50)
    def __str__ (self):
        return f"{self.first_steps}"
class SecondSteps(models.Model):
    seconds_steps = models.CharField(max_length=50)
    def __str__ (self):
        return f"{self.seconds_steps}"
class ThirdSteps(models.Model):
    third_steps = models.CharField(max_length=50)
    def __str__ (self):
        return f"{self.third_steps}"
class FourthSteps(models.Model):
    fourth_steps = models.CharField(max_length=50)
    def __str__ (self):
        return f"{self.fourth_steps}"
    

class CareerPath(models.Model):
    # CareerPath_CHOICES = [
    #     ('penetraion testing','Penetraion Testing'),
    #     ('blue teaming', 'Blue Teaming'),
    #     ('red teaming', 'Rlue Teaming'),
    #     # ... other choices
    # ]
    Paths = models.CharField(max_length=50)
    describition = models.TextField(max_length=300,default="",null=False,blank=False)
    image = models.ImageField(upload_to='career_path_images/', blank=True, null=True)

    def __str__ (self):
        return f"{self.Paths}"
    
class RoadMap(models.Model):
    path = models.ForeignKey(CareerPath, related_name='path',on_delete=models.CASCADE,default=1)
    html_file = models.CharField(max_length=250,default="")
    def __str__ (self):
        return f"{self.path}'s Roadmap"
    


class EventsAndWorkshops(models.Model):
    Price = models.DecimalField(max_digits=9,decimal_places=2,default=0)
    event = models.CharField(max_length=100)
    EventTime = models.TimeField(null=False,blank=False)
    EventDate = models.DateField(null=False,blank=False)
    Deadline = models.DateField(null=True,blank=True)
    Eventplace = models.CharField(max_length=100,null=False,blank=False)
    EventPath = models.ManyToManyField(CareerPath, blank=False, related_name="EventsAndWorkshops")
    image = models.ImageField(upload_to='event_images/', blank=True, null=True)

    def __str__ (self):
        return f"{self.event}"

class Company(models.Model):
    # COMPANY_CHOICES = [
    #     ('company1', 'Company 1'),
    #     ('company2', 'Company 2'),
    #     # ... other choices
    # ]
    CompanyName = models.CharField(max_length=50)
    image = models.ImageField(upload_to='company_images/', blank=True, null=True)

    def __str__ (self):
        return f"{self.CompanyName}"

class Training(models.Model):
    TrainingName = models.CharField(max_length=100)
    TrainingDate = models.DateField(null=False,blank=False,default=now)
    TrainingTime = models.TimeField(null=False,blank=False,default=now)
    TrainingPlace = models.CharField(max_length=100)
    TrainingCompany = models.ManyToManyField(Company, blank=True, related_name="Training")
    image = models.ImageField(upload_to='training_images/', blank=True, null=True)

    def __str__ (self):
        return f"{self.TrainingName}"
    

class Course(models.Model):
    CourseName = models.CharField(max_length=100)
    author = models.CharField(max_length=150,null=True,blank=True,default="zero")
    RelatedEvents = models.ManyToManyField(EventsAndWorkshops, blank=True, related_name="Courses")
    image = models.ImageField(upload_to='course_images/', blank=True, null=True)
    Path = models.ManyToManyField(CareerPath, blank=False, related_name="Courses")
    link  = models.CharField(blank=False,null=False, max_length=1000,default="https://www.youtube.com/watch?v=4sYNBViSq-8")

    def __str__ (self):
        return f"{self.CourseName}"

class Jobs(models.Model):
    JobName = models.CharField(max_length=100)
    JobDiscribtion = models.TextField()
    JobTraining = models.ManyToManyField(Training)
    JobAssociations = models.ManyToManyField(CareerPath)
    image = models.ImageField(upload_to='job_images/', blank=True, null=True)

    def __str__ (self):
        return f"{self.JobName}"




