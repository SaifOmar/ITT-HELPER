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

# class TrainingForm(ModelForm):
#     TrainingDate= forms.DateField(
#         label='Training Date',
#         widget=forms.widgets.DateInput(attrs={'type':'date'})
#     )
#     TrainingTime= forms.TimeField(
#         label='Training Time',
#         widget=forms.widgets.TimeInput(attrs={'type':'time'})
#     )
#     class Meta :
#         model = Training
#         fields = "__all__"



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
            'image': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
        }



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
