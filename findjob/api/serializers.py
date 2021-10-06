from rest_framework import serializers
from projects.models import Project, Tag
from users.models import Student, User, Lecture
from jobs.models import JobPost, Need, Application


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class LectureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lecture
        fields = ['username']


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class NeedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Need
        fields = '__all__'


class ProjectSerializer(serializers.ModelSerializer):
    owner = serializers.SlugRelatedField(
        queryset=Student.objects.all(),
        slug_field='username',
        required=True
    )

    tags = TagSerializer(many=True, read_only=True)

    class Meta:
        model = Project
        fields = '__all__'


class JobPostSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        queryset=Lecture.objects.all(),
        slug_field='username',
        required=True
    )

    jobs_tags = NeedSerializer(many=True, read_only=True)

    class Meta:
        model = JobPost
        fields = '__all__'


class ApplicationSerializer(serializers.ModelSerializer):
    jobpost = serializers.SlugRelatedField(
        queryset=JobPost.objects.all(),
        slug_field='title',
        required=True
    )
    applicant = serializers.SlugRelatedField(
        queryset=Student.objects.all(),
        slug_field='username',
        required=True
    )
    is_checked = serializers.SlugRelatedField(
        queryset=Lecture.objects.all(),
        slug_field='username',
        required=True
    )

    class Meta:
        model = Application
        fields = '__all__'
