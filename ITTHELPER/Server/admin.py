from django.contrib import admin
from .models import Course,CareerPath,Jobs,Company,Training,EventsAndWorkshops,FirstSteps,SecondSteps,ThirdSteps,FourthSteps,RoadMap
from accounts.models import CustomUser
# Register your models here.
admin.site.register(Course)
admin.site.register(CareerPath)
admin.site.register(Training)
admin.site.register(Jobs)
admin.site.register(EventsAndWorkshops)
admin.site.register(Company)
admin.site.register(CustomUser)
admin.site.register(FirstSteps)
admin.site.register(SecondSteps)
admin.site.register(ThirdSteps)
admin.site.register(FourthSteps)
admin.site.register(RoadMap)