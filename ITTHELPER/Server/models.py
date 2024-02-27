from django.db import models

# Create your models here.
# note make models for courses /career paths/events/...
# many to many relations 

class CareerPath(models.Model):
    CareerPath_CHOICES = [
        ('path1', 'Path 1'),
        ('path2', 'Path 2'),
        # ... other choices
    ]
    CompanyName = models.CharField(max_length=50, choices=CareerPath_CHOICES)

class EventsAndWorkshops(models.Model):
    event = models.CharField(max_length=100)
    EventTime = models.TimeField()
    Eventplace = models.CharField(max_length = 100)
    EventPath = models.ManyToManyField(CareerPath, blank = False , related_name= "EventsAndWorkshops")

class Company(models.Model):
    COMPANY_CHOICES = [
        ('company1', 'Company 1'),
        ('company2', 'Company 2'),
        # ... other choices
    ]
    CompanyName = models.CharField(max_length=50, choices=COMPANY_CHOICES)

class Training(models.Model):
    TrainingName = models.CharField(max_length=100)
    TrainingTime = models.TimeField()
    TrainingPlace = models.CharField(max_length = 100)
    TrainingCompany = models.ManyToManyField(Company,blank = True, null= True, related_name="Training" )



class Course(models.Model):
    CourseName = models.CharField(max_length=100)
    Path = models.ManyToManyField(CareerPath, blank = False, related_name="Courses")
    RelatedEvents = models.ManyToManyField(EventsAndWorkshops, blank= True, related_name="Courses")
    

class Jobs(models.Model):
    JobName = models.CharField(max_length=100)
    JobDiscribtion = models.TextField()
    JobTraining = models.ManyToManyField(Training)
    JobAssociations = models.ManyToManyField(CareerPath)




