from django.urls import path
from rest_framework import routers
from . import views 
from Server.models import Course,Company,EventsAndWorkshops,Jobs,CareerPath,Training
from .serilalizers import CompanySerializer,CourseSerializer,JobsSerializer,EventsSerializer,TrainingSerializer,PathSerializer
# Create your views here.

router = routers.DefaultRouter()
# router.register(r'users', UserViewSet)
# router.register(r'accounts', AccountViewSet)
# router.register(r'courses',views.course_view)

urlpatterns = [
    # path('forgot-password/', ForgotPasswordFormView.as_view()),
    # i dont think we should need the queryset and serializer class 
    path('courses',views.course_view.as_view(queryset= Course.objects.all(),serializer_class = CourseSerializer)) ]
    

urlpatterns += router.urls