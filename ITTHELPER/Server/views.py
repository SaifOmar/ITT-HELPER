from django.shortcuts import render, get_object_or_404,redirect
from .models import Course , Training , EventsAndWorkshops,  Jobs, CareerPath
from .forms import CourseForm,CareerPathForm,JobsForm,TrainingForm,EventsForm
from django.contrib.auth import authenticate,login,logout

# Create your views here.


# rendering views
def HomeView(request):
    return render(request,'home.html')

def TrainingView(request):
    training = Training.objects.all()
    return render(request, "training.html", {"training": training})

def EventsView(request):
    events = EventsAndWorkshops.objects.all()
    return render(request, "events.html", {"events": events})

def CoursesView(request):
    courses = Course.objects.all()
    return render(request,"courses.html" , {"courses":courses})

def JobsView(request):
    jobs = Jobs.objects.all()
    return render(request, "jobs.html",{"job":jobs})

def CareerPathView(request):
    return render(request,'path.html')
    

def CVView(request):
    return render(request, "cv.html")

def EmploymentView(request):
    return render(request, "employment.html")

def InterviewGuidesView(request):
    return render(request,"guides.html")

# detailed views
def TrainingDetailView(request,id):
    triaining_detail = Training.objects.get(id=id)
    return render(request, 'training_detail', {'training': triaining_detail})

def EvnetDetailView(request,id):
    events_detail=EventsAndWorkshops.objects.get(id=id)
    return render(request,'events_detail.html', {"events": events_detail})

def CourseDetialView(request,id):
    course_detail = Course.objects.get(id=id)
    return render(request, "coursedetial.html" , {'course':course_detail})

# creation of objects
def AddCoursesView(request):
    form = CourseForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect(CoursesView)
        else:
            return render(request, "addcourses.html",{"form":form})
    return render(request,"addcourses.html",{"form":form})

def AddCareerPathView(request):
    form = CareerPathForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect(CareerPathView)
        else:
            return render(request,"addcareerpaths.html",{"form":form})
    return render(request,"addcareerpaths.html",{"form":form})

def AddJobView(request):
    form = JobsForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect(JobsView)
        else:
            return render(request,"addjobs.html",{"form":form})
    return render(request,"addjobs.html",{"form":form}) 

def AddTrainingView(request):
    form = TrainingForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            form.save()
        else:
            return render(request,"addtraining.html",{"form":form})
    return render(request,"addtraining.html",{"form":form}) 

def AddEvents(request):
    form = EventsForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            form.save()
        else:
            return render(request,"addevents.html",{"form":form})
    return render(request,"addevents.html",{"form":form})

# updating objects

def UpdateCourse(request,id):
    obj = get_object_or_404(id=id)
    pass

def UpdateJob(request,id):
    obj = get_object_or_404(id=id)
    pass

def UpdateCareerPath():
    obj = get_object_or_404(id=id)
    pass

def UpdateEvents():
    obj = get_object_or_404(id=id)
    pass

def UpdateTraining():
    obj = get_object_or_404(id=id)
    pass


#  deleting objects
def DeleteCourse(request):
    if request.method == "DELETE":
        obj = Course.objects.get(id=id)
        obj.delete()
        return redirect(CoursesView)
    
def DeleteJob(request):
    if request.method == "DELETE":
        obj = Course.objects.get(id=id)
        obj.delete()
        return redirect(JobsView)

def DeleteCareerPath(request):
    if request.method == "DELETE":
        obj = Course.objects.get(id=id)
        obj.delete()
        return redirect(CareerPathView)
    
def DeleteEvents(request):
   if request.method == "DELETE":
        obj = Course.objects.get(id=id)
        obj.delete()
        return redirect(EventsView)
    
def DeleteTraining(request):
    if request.method == "DELETE":
        obj= Training.objects.get(id=id)
        obj.delete()
        return redirect(TrainingView)



           
