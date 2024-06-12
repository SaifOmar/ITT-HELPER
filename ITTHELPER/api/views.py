from django.shortcuts import render
from rest_framework.views import APIView
from Server.models import Course,Company,EventsAndWorkshops,Jobs,CareerPath,Training
from .serilalizers import CompanySerializer,CourseSerializer,JobsSerializer,EventsSerializer,TrainingSerializer,PathSerializer
from rest_framework.decorators import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny,DjangoModelPermissionsOrAnonReadOnly
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

# Create your views here.
class course_view(ModelViewSet):
    permission_classes = [IsAuthenticated,DjangoModelPermissionsOrAnonReadOnly]
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
# there is an error here empty objects
class job_view(ModelViewSet):
    permission_classes = [IsAuthenticated,DjangoModelPermissionsOrAnonReadOnly]
    queryset = Jobs.objects.all()
    serializer_class = JobsSerializer

class events_view(ModelViewSet):
    permission_classes = [IsAuthenticated,DjangoModelPermissionsOrAnonReadOnly]
    queryset = EventsAndWorkshops.objects.all()
    serializer_class = EventsSerializer

class training_view(ModelViewSet):
    permission_classes = [IsAuthenticated,DjangoModelPermissionsOrAnonReadOnly]
    queryset = Training.objects.all()
    serializer_class = TrainingSerializer

class path_view(ModelViewSet):
    permission_classes = [IsAuthenticated,DjangoModelPermissionsOrAnonReadOnly]
    queryset = CareerPath.objects.all()
    serializer_class = PathSerializer

class company_view(ModelViewSet):
    permission_classes = [IsAuthenticated,DjangoModelPermissionsOrAnonReadOnly]
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

class contact_us(APIView):
    permission_classes = [AllowAny]
    def post(self,request):
        name = request.data["name"]
        email = request.data["email"]
        text = request.data["text"]
        f = open("/Server/ContactUs.txt","a")
        f.write(name+" "+email+" "+ text)
        f.close()
        return Response({"response":"Thank you for contacting us"}) 

class feedback(APIView):
    permission_classes=[IsAuthenticated]
    def post(self,request):
        user = request.user.first_name
        email = request.user.email
        text = request.data["text"]
        f = open ("/Server/Feedback.txt","a")
        f.write(user+" "+email+" "+ text)
        f.close
        return Response({"response":"Thank you for your feedback"})
