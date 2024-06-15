from django.shortcuts import render, get_object_or_404,redirect,HttpResponse
from .models import Course , Training , EventsAndWorkshops,  Jobs, CareerPath
from .forms import CourseForm,CareerPathForm,JobsForm,TrainingForm,EventsForm
from django.contrib.auth.decorators import permission_required, login_required
from django.contrib import messages
from django.core.exceptions import PermissionDenied
from django.contrib.auth.models import Permission
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
    cp = CareerPath.objects.all()
    return render(request,'path.html',{"cp" : cp})
    

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


def EventDetailView(request,id):
    events_detail=EventsAndWorkshops.objects.get(id=id)
    return render(request,'events_detail.html', {"events": events_detail})
    

def CourseDetialView(request,id):
    course_detail = Course.objects.get(id=id)
    return render(request, "coursedetail.html" , {'course':course_detail})

def JobDetialView(request,id):
    Job_detail = Jobs.objects.get(id=id)
    return render(request, "jopdetail.html" , {'course':Job_detail})

# creation of objects
@login_required
def AddCoursesView(request):
    if not request.user.is_superuser :
        return HttpResponse("<h1>You don't have permission!</h1>")
    form = CourseForm(request.POST,request.FILES)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect(CoursesView)
        else:
            return render(request, "addcourse.html",{"form":form})
    return render(request,"addcourse.html",{"form":form})

@login_required
def AddCareerPathView(request):
    if not request.user.is_superuser :
        return HttpResponse("<h1>You don't have permission!</h1>")
    form = CareerPathForm(request.POST,request.FILES)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect(CareerPathView)
        else:
            return render(request,"addpath.html",{"form":form})
    return render(request,"addpath.html",{"form":form})
@login_required
def AddJobView(request):
    if not request.user.is_superuser :
        return HttpResponse("<h1>You don't have permission!</h1>")
    form = JobsForm(request.POST,request.FILES)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect(JobsView)
        else:
            return render(request,"addjobs.html",{"form":form})
    return render(request,"addjobs.html",{"form":form}) 

@login_required
def AddTrainingView(request):
    if not (request.user.is_company or request.user.is_superuser or request.user.is_staff)  :
        return HttpResponse("<h1>You don't have permission</h1>")
    form = TrainingForm(request.POST,request.FILES)
    if request.method == "POST" :
        if form.is_valid():
            form.save()
        else:
            return render(request,"addtraining.html",{"form":form})
    return render(request,"addtraining.html",{"form":form}) 

@login_required
def AddEvents(request):
    if not request.user.is_superuser :
        return HttpResponse("<h1>You don't have permission!</h1>")
    form = EventsForm(request.POST,request.FILES)
    if request.method == "POST":
        if form.is_valid():
            form.save()
        else:
            return render(request,"addevents.html",{"form":form})
    return render(request,"addevents.html",{"form":form})


#  deleting objects
@login_required
def DeleteCourse(request,id):
    if not request.user.is_superuser :
        return HttpResponse("<h1>You don't have permission!</h1>")
    if request.method == "DELETE":
        obj = Course.objects.get(id=id)
        obj.delete()
        return redirect(CoursesView)
@login_required
def DeleteJob(request,id):
    if not request.user.is_superuser :
        return HttpResponse("<h1>You don't have permission!</h1>")
    if request.method == "DELETE":
        obj = Course.objects.get(id=id)
        obj.delete()
        return redirect(JobsView)

@login_required
def DeleteCareerPath(request,id):
    if not request.user.is_superuser :
        return HttpResponse("<h1>You don't have permission!</h1>")
    if request.method == "DELETE":
        obj = Course.objects.get(id=id)
        obj.delete()
        return redirect(CareerPathView)

@login_required
def DeleteEvents(request,id):
   if not request.user.is_superuser :
        return HttpResponse("<h1>You don't have permission!</h1>")
   if request.method == "DELETE":
        obj = Course.objects.get(id=id)
        obj.delete()
        return redirect(EventsView)
    
@login_required
def DeleteTraining(request, id):
    if not request.user.is_superuser :
        return HttpResponse("<h1>You don't have permission!</h1>")
    if request.method == "DELETE":
        obj= Training.objects.get(id=id)
        obj.delete()
        return redirect(TrainingView)



def ContactUs(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        phone = request.POST.get("phone")
        message = request.POST.get("message")
        f = open ("ContactUs.txt", "a")
        f.write(f"[{name},{phone},{subject},{email},{message}], ")
        f.close()
    return render(request,"contact-us.html")
            



def FeedBack(request):
    if not request.user.is_authenticated :
        return redirect('login')
    
    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        date = request.POST.get("date")
        ltype = request.POST.get("type")
        email = request.POST.get("email")
        message = request.POST.get("message")
        position = request.POST.get("position")
        print(name,phone,date,ltype,email,message,position)
        f = open("Feedback.txt", "a")
        f.write(f"[{name},{phone},{date},{ltype},{email},{message},{position}], ")
        f.close()
    return render(request,"feedback.html")   

def ChatBot(request):
    return render (request, "chatbot.html")

def RoadMap_pentesting(request):
    return render(request, "roadmap-pentest.html")
def RoadMap_blue_teaming(request):
    return render(request, "roadmap-blue.html")
def RoadMap_red_teaming(request):
    return render(request, "roadmap-red.html")




# updates



# @login_required       
# def UpdateJob(request,id):
#     obj = get_object_or_404(id=id)
#     form = EventsForm(request.POST, instance=obj)
#     if request.method == "POST":
#         if form.is_valid():
#             form.save()
#         else:
#             return render(request,"addcourse.html", {"form": form})
#         return render(request,"events.html")
#     return render(request,"addcourse.html", {"form": form})
# @login_required
# @permission_required("server.can_change_CareerPath")
# def UpdateCareerPath(request,id):
#     obj = get_object_or_404(id=id)
#     form = EventsForm(request.POST, instance=obj)
#     if request.method == "POST":
#         if form.is_valid():
#             form.save()
#         else:
#             return render(request,"addcourse.html", {"form": form})
#         return render(request,"events.html")
#     return render(request,"addcourse.html", {"form": form})
# @login_required
# @permission_required("server.can_change_EventsAndWorkshops")
# def UpdateEvents(request,id):
#     obj = get_object_or_404(id=id)
#     form = EventsForm(request.POST, instance=obj)
#     if request.method == "POST":
#         if form.is_valid():
#             form.save()
#         else:
#             return render(request,"addcourse.html", {"form": form})
#         return render(request,"events.html")
#     return render(request,"addcourse.html", {"form": form})

# @login_required
# def UpdateCourse(request,id):
#     obj = get_object_or_404(id=id)
#     form = EventsForm(request.POST, instance=obj)
#     if request.method == "POST":
#         if form.is_valid():
#             form.save()
#         else:
#             return render(request,"addcourse.html", {"form": form})
#         return render(request,"events.html")
#     return render(request,"addcourse.html", {"form": form})
# @login_required
# @permission_required("server.can_change_Training")
# def UpdateTraining(request,id):
#     obj = get_object_or_404(id=id)
#     form = EventsForm(request.POST, instance=obj)
#     if request.method == "POST":
#         if form.is_valid():
#             form.save()
#         else:
#             return render(request,"addcourse.html", {"form": form})
#         return render(request,"events.html")
#     return render(request,"addcourse.html", {"form": form})