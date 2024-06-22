from django.urls import path
from rest_framework import routers
from . import views 
from Server.models import Course,Company,EventsAndWorkshops,Jobs,CareerPath,Training
from .serilalizers import CompanySerializer,CourseSerializer,JobsSerializer,EventsSerializer,TrainingSerializer,PathSerializer
# Create your views here.

router = routers.DefaultRouter()
# router.register(r"",views.mai)
router.register(r"courses", views.course_view)
router.register(r"companies", views.company_view)
router.register(r"jobs", views.job_view)
router.register(r"paths", views.path_view)
router.register(r"training", views.training_view)
router.register(r"events", views.events_view)


urlpatterns = [
    path("contact-us", views.contact_us.as_view(), name="conatact_us"),
    path("feedback", views.feedback.as_view(), name="feedback")
    # path('forgot-password/', ForgotPasswordFormView.as_view()), 
    ]
    

urlpatterns += router.urls