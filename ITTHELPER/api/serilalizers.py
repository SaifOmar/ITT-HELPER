from Server.models import Course,Company,EventsAndWorkshops,Jobs,CareerPath,Training


from rest_framework import serializers

class CourseSerializer(serializers.ModelSerializer):
    class Meta : 
        model = Course
        fields = "__all__"


class CompanySerializer(serializers.ModelSerializer):
    class Meta : 
        model = Company
        feilds = "__all__"


class EventsSerializer(serializers.ModelSerializer):
    class Meta : 
        model = EventsAndWorkshops
        feilds = "__all__"


class JobsSerializer(serializers.ModelSerializer):
    class Meta : 
        model = Jobs
        feilds = "__all__"


class TrainingSerializer(serializers.ModelSerializer):
    class Meta : 
        model = Training
        feilds = "__all__"



class PathSerializer(serializers.ModelSerializer):
    class Meta : 
        model = CareerPath
        feilds = "__all__"

