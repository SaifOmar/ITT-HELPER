from django.urls import path 
from . import views 


urlpatterns = [
    path('', views.HomeView ,name="home" ),
    path('training', views.TrainingView ,name="training" ),
    path('events', views.EventsView ,name="events" ),
    

]