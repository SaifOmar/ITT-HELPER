from .models import Course,CareerPath,EventsAndWorkshops,Jobs,Training
from django.forms import ModelForm
from django import forms

class CourseForm(ModelForm):
    class Meta : 
        model = Course 
        fields = "__all__"

    


class CareerPathForm(ModelForm):
    class Meta :
        model = CareerPath
        fields = "__all__"

class TrainingForm(ModelForm):
    TrainingDate= forms.DateField(
        label='Training Date',
        widget=forms.widgets.DateInput(attrs={'type':'date'})
    )
    TrainingTime= forms.TimeField(
        label='Training Time',
        widget=forms.widgets.TimeInput(attrs={'type':'time'})
    )
    class Meta :
        model = Training
        fields = "__all__"

class JobsForm(ModelForm):
    class Meta :
        model = Jobs
        fields = "__all__"

class EventsForm(ModelForm):
    EventTime = forms.TimeField(
        label="Event Time",
        widget=forms.widgets.TimeInput(attrs={'type':'time'})
    )
    EventDate = forms.DateField(
        label="Event Date",
        widget=forms.widgets.DateInput(attrs={'type':'date'})
    )
    Deadline = forms.DateField(
        label="Event Deadline",
        widget=forms.widgets.DateInput(attrs={'type':'date'})
    )

    class Meta :
        model = EventsAndWorkshops
        fields = "__all__"
