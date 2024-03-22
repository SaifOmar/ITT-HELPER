from django.contrib import admin
from .models import Course,CareerPath,Jobs,Company,Training,EventsAndWorkshops
from accounts.models import CustomUser
# Register your models here.
admin.site.register(Course)
admin.site.register(CareerPath)
admin.site.register(Training)
admin.site.register(Jobs)
admin.site.register(EventsAndWorkshops)
admin.site.register(Company)
admin.site.register(CustomUser)