from django.shortcuts import render

# Create your views here.
def HomeView(request):
    return render(request,'home.html')

def TrainingView(request):
    return render(request, "training.html")

def EventsView(request):
    return render(request, "events.html")

def CoursesView(request):
    pass

def CareerPathView(request):
    pass

def CVView(request):
    pass

def EmploymentView(request):
    pass

def InterviewGuidesView(request):
    pass

def RegisterUser(request):
    return render(request, "regitration.html")

def LoginUser(request):
    pass

def LogoutUser(request):
    pass