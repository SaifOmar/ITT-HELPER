from django.shortcuts import render
from rest_framework.views import APIView
from Server.models import Course,Company,EventsAndWorkshops,Jobs,CareerPath,Training
from .serilalizers import CompanySerializer,CourseSerializer,JobsSerializer,EventsSerializer,TrainingSerializer,PathSerializer
from rest_framework.decorators import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

# Create your views here.
class course_view(ModelViewSet):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
# there is an error here empty objects
class job_view(ModelViewSet):
    permission_classes = [AllowAny]
    queryset = Jobs.objects.all()
    serializer_class = JobsSerializer

class events_view(ModelViewSet):
    permission_classes = [AllowAny]
    queryset = EventsAndWorkshops.objects.all()
    serializer_class = EventsSerializer

class training_view(ModelViewSet):
    permission_classes = [AllowAny]
    queryset = Training.objects.all()
    serializer_class = TrainingSerializer

class path_view(ModelViewSet):
    permission_classes = [AllowAny]
    queryset = CareerPath.objects.all()
    serializer_class = PathSerializer

class company_view(ModelViewSet):
    permission_classes = [AllowAny]
    queryset = Company.objects.all()
    serializer_class = CompanySerializer