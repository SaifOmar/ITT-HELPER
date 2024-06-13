from .models import Course,CareerPath,EventsAndWorkshops,Jobs,Training
from django.forms import ModelForm

class CourseForm(ModelForm):
    class Meta : 
        model = Course 
        fields = "__all__"

    


class CareerPathForm(ModelForm):
    class Meta :
        model = CareerPath
        fields = "__all__"

class TrainingForm(ModelForm):
    class Meta :
        model = Training
        fields = "__all__"

class JobsForm(ModelForm):
    class Meta :
        model = Jobs
        fields = "__all__"

class EventsForm(ModelForm):
    class Meta :
        model = EventsAndWorkshops
        fields = "__all__"
