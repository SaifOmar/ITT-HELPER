from .models import Course,CareerPath,EventsAndWorkshops,Jobs,Training
from django.forms import ModelForm
from django import forms

class CourseForm(ModelForm):
    class Meta : 
        model = Course 
        fields = "__all__"
        widgets = {
            'CourseName': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control'}),
            'RelatedEvents': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'Path': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'link': forms.URLInput(attrs={'class': 'form-control'}),
        }

    
class JobsForm(ModelForm):
    pass

class CareerPathForm(ModelForm):
    class Meta :
        model = CareerPath
        fields = "__all__"
        widgets = {
            'Paths': forms.TextInput(attrs={'class': 'form-control'}),
            'describition': forms.Textarea(attrs={'class': 'form-control'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }


class TrainingForm(forms.ModelForm):
    class Meta:
        model = Training
        fields = "__all__"
        widgets = {
            'TrainingName': forms.TextInput(attrs={'class': 'form-control'}),
            'TrainingDate': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'TrainingTime': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'TrainingPlace': forms.TextInput(attrs={'class': 'form-control'}),
            'TrainingCompany': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }


class EventsForm(ModelForm):
    EventTime = forms.TimeField(
        label="Event Time",
        widget=forms.widgets.TimeInput(attrs={'type':'time', 'class': 'form-control'})
    )
    EventDate = forms.DateField(
        label="Event Date",
        widget=forms.widgets.DateInput(attrs={'type':'date', 'class': 'form-control'})
    )
    Deadline = forms.DateField(
        label="Event Deadline",
        widget=forms.widgets.DateInput(attrs={'type':'date', 'class': 'form-control'})
    )

    class Meta :
        model = EventsAndWorkshops
        fields = "__all__"
        widgets = {
            'Price': forms.NumberInput(attrs={'class': 'form-control'}),
            'event': forms.TextInput(attrs={'class': 'form-control'}),
            'Eventplace': forms.TextInput(attrs={'class': 'form-control'}),
            'EventPath': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }
