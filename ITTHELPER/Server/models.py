from django.db import models
# Create your models here.
# note make models for courses /career paths/events/...
# many to many relations 
CareerPath_CHOICES = [
        ('path1', 'Path 1'),
        ('path2', 'Path 2'),
        # ... other choices
    ]

class CareerPath(models.Model):
    Paths = models.CharField(max_length=50, choices=CareerPath_CHOICES)
    
    def __str__ (self):
        return f"{self.Paths}"

    

class EventsAndWorkshops(models.Model):
    event = models.CharField(max_length=100)
    EventTime = models.TimeField()
    Eventplace = models.CharField(max_length = 100)
    EventPath = models.ManyToManyField(CareerPath, blank = False , related_name= "EventsAndWorkshops")

    def __str__ (self):
        return f"{self.event}"
    
class Company(models.Model):
    COMPANY_CHOICES = [
        ('company1', 'Company 1'),
        ('company2', 'Company 2'),
        # ... other choices
    ]
    CompanyName = models.CharField(max_length=50, choices=COMPANY_CHOICES)


    def __str__ (self):
        return f"{self.CompanyName}"
    

class Training(models.Model):
    TrainingName = models.CharField(max_length=100)
    TrainingTime = models.TimeField()
    TrainingPlace = models.CharField(max_length = 100)
    TrainingCompany = models.ManyToManyField(Company,blank = True,  related_name="Training" )

    def __str__ (self):
        return f"{self.TrainingName}"

class Course(models.Model):
    CourseName = models.CharField(max_length=100)
    Path = models.ManyToManyField(CareerPath, blank = False, related_name="Courses")
    RelatedEvents = models.ManyToManyField(EventsAndWorkshops, blank= True, related_name="Courses")
    
    def __str__ (self):
        return f"{self.CourseName}"

class Jobs(models.Model):
    JobName = models.CharField(max_length=100)
    JobDiscribtion = models.TextField()
    JobTraining = models.ManyToManyField(Training)
    JobAssociations = models.ManyToManyField(CareerPath)

    def __str__ (self):
        return f"{self.JobName}"




