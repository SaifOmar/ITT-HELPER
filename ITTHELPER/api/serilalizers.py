from Server.models import Course,Company,EventsAndWorkshops,Jobs,CareerPath,Training


from rest_framework import serializers

class CourseSerializer(serializers.ModelSerializer):
    class Meta : 
        model = Course
        fields = "__all__"


class CompanySerializer(serializers.ModelSerializer):
    class Meta : 
        model = Company
        fields = "__all__"


class EventsSerializer(serializers.ModelSerializer):
    class Meta : 
        model = EventsAndWorkshops
        fields = "__all__"


class JobsSerializer(serializers.ModelSerializer):
    class Meta : 
        model = Jobs
        fields = "__all__"


class TrainingSerializer(serializers.ModelSerializer):
    class Meta : 
        model = Training
        fields = "__all__"



class PathSerializer(serializers.ModelSerializer):
    class Meta : 
        model = CareerPath
        fields = "__all__"

