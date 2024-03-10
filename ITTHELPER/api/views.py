from django.shortcuts import render
from rest_framework import views , viewsets ,generics
from rest_framework.views import APIView
from Server.models import Course,Company,EventsAndWorkshops,Jobs,CareerPath,Training
from .serilalizers import CompanySerializer,CourseSerializer,JobsSerializer,EventsSerializer,TrainingSerializer,PathSerializer
from rest_framework.decorators import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
# Create your views here.
class course_view(generics.ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
# there is an error here empty objects
    

