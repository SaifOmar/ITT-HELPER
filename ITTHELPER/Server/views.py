from django.shortcuts import render, get_object_or_404,redirect
from .models import Course , Training , EventsAndWorkshops,  Jobs, CareerPath
from .forms import CourseForm,CareerPathForm,JobsForm,TrainingForm,EventsForm
# Create your views here.
def HomeView(request):
    return render(request,'home.html')

def TrainingView(request):
    training = Training.objects.all()
    return render(request, "training.html", {
        "training": training
    })

def TrainingDetailView(request,id):
    triaining_detail = Training.objects.get(id=id)
    return render(request, 'training_detail', {'training': triaining_detail})

def EventsView(request):
    events = EventsAndWorkshops.objects.all()
    return render(request, "events.html", {"events": events})

def EvnetDetailView(request,id):
    events_detail=EventsAndWorkshops.objects.get(id=id)
    return render(request,'events_detail.html', {"events": events_detail})

def CoursesView(request):
    courses = Course.objects.all()
    return render(request,"courses.html" , {"course":courses})

def CourseDetialView(request,id):
    course_detail = Course.objects.get(id=id)
    return render(request, "coursedetial.html" , {'course':course_detail})

def CareerPathView(request):
    careerpath = CareerPath.objects.all()
    return render(request, "careerpaths.html", {"careerpath": careerpath})

def AddCoursesView(request):
    form = CourseForm()
    if request.method == "POST":
        if form.is_valid():
            form.save()
    return render(request,"addcourses.html")


def AddCareerPathView(request):
    form = CareerPathForm()
    if request.method == "POST":
        if form.is_valid():
            form.save()
        else:
            return render(request)
    return render(request,"addcareerpaths.html")



def AddJobView(request):
    form = JobsForm()
    if request.method == "POST":
        if form.is_valid():
            form.save()
        else:
            return render(request)
    return render(request,"addjobs.html") 



def AddTrainingView(request):
    form = TrainingForm()
    if request.method == "POST":
        if form.is_valid():
            form.save()
        else:
            return render(request)
    return render(request,"addtraining.html") 



def AddEvents(request):
    form = EventsForm()
    if request.method == "POST":
        if form.is_valid():
            form .save()
        else:
            return
    return render(request,"addevents.html")

def CVView(request):
    return render(request, "cv.html")

def EmploymentView(request):
    return render(request, "employment.html")

def InterviewGuidesView(request):
    return render(request,"guides.html")
