from rest_framework import serializers
from projects.models import Project, Tag
from users.models import Student, User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class StudentSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False)

    class Meta:
        model = Student
        fields = '__all__'


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class ProjectSerializer(serializers.ModelSerializer):
    owner = StudentSerializer(many=False)
    tags = TagSerializer(many=True)

    class Meta:
        model = Project
        fields = '__all__'
