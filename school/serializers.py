from rest_framework import serializers
from .models import School, Classes, Student
from django.contrib.auth import authenticate

class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['classes'] = ClassesSerializer(instance.classs.all(),
                                                      many=True).data
        return representation


class ClassesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classes
        fields = '__all__'


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('name', 
                  'email', 
                  'date_of_birth', 
                  'classes', 
                  'address', 
                  'gender', 
                  'photo')

    

