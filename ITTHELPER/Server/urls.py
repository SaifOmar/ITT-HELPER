from django.urls import path 
from . import views 


urlpatterns = [

    path('', views.HomeView ,name="home" ),
    path('training', views.TrainingView ,name="training" ),
    path('events', views.EventsView ,name="events" ),
    path('path', views.CareerPathView, name ="path"),
    path('jobs',views.JobsView,name = 'jobs'),
    path('courses',views.CoursesView,name = 'courses'),
    path('employment',views.EmploymentView,name="employment"),
    path('cv',views.CVView,name="cv"),
    path('guides',views.InterviewGuidesView,name="guides"),
    path("contact-us", views.ContactUs,name="contact_us"),
    path("feedback", views.FeedBack,name="feedback"),
    path("chatbot", views.ChatBot,name="chatbot"),

    path('courses/create',views.AddCoursesView,name="create_course"),
    path('jobs/create',views.AddJobView,name="create_job"),
    path('training/create',views.AddTrainingView,name="create_training"),
    path('careerpath/create',views.AddCareerPathView,name="create_path"),
    path('events/create',views.AddEvents,name="create_event"),

    path('courses/delete/<int:id>',views.DeleteCourse,name="del_course"),
    path('jobs/delete/<int:id>',views.DeleteJob,name="del_job"),
    path('training/delete/<int:id>',views.DeleteTraining,name="del_training"),
    path('careerpath/delete/<int:id>',views.DeleteCareerPath,name="del_path"),
    path('events/delete/<int:id>',views.DeleteEvents,name="del_event"),

    path("courses/<int:id>",views.CourseDetialView,name ="courses_detail"),
    path("jobs/<int:id>",views.JobDetialView,name ="Job_detail"),
    path("training/<int:id>",views.TrainingDetailView,name ="training_detail"),
    path("events/<int:id>",views.EventDetailView,name ="events_detail"),
     

]