from django.db import models

# Create your models here.
# note make models for courses /career paths/events/...
# many to many relations 

class CareerPath(models.Model):
    Path = models.TextChoices()

class EventsAndWorkshops(models.Model):
    event = models.CharField(max_lenght=100)
    EventTime = models.TimeField()
    Eventplace = models.CharField(max_lenght = 100)
    EventPath = models.ManyToManyField(CareerPath, blank = False , related_name= "EventsAndWorkshops")

class Company(models.Model):
    CompanyName = models.TextChoices()

class Training(models.Model):
    TrainingName = models.CharField(max_length=100)
    TrainingTime = models.TimeField()
    TrainingPlace = models.CharField(max_length = 100)
    TrainingCompany = models.ManyToManyField(Company,blank = True, null= True, related_name="Training" )



class Course(models.Model):
    CourseName = models.CharField(max_length=100)
    Path = models.ManyToManyField(CareerPath, blank = False, related_name="Courses")
    RelatedEvents = models.ForeignKey(EventsAndWorkshops, blank= True, related_name="Courses")
    

class Jobs(models.Model):
    JobName = models.CharField()
    JobDiscribtion = models.TextField()
    JobTrack = models.ManyToManyField(CareerPath)
    JobRelatedEvents = models.ManyToManyField(EventsAndWorkshops)
    JobTraining = models.ManyToManyField(Training)