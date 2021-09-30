from django import forms
from django.db.models.base import Model
from django.forms import ModelForm
from .models import JobPost, Application
from users.models import Lecture


class LectureProfileForm(ModelForm):
    class Meta:
        model = Lecture
        fields = ['email', 'username',
                  'location', 'short_intro', 'profile_image']

    def __init__(self, *args, **kwargs):
        super(LectureProfileForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})


class JobPostForm(ModelForm):
    class Meta:
        model = JobPost
        exclude = ['id', 'created', 'archived', 'author']

    def __init__(self, *args, **kwargs):
        super(JobPostForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})


class ApplicationForm(ModelForm):
    class Meta:
        model = Application
        exclude = ['id', 'applicant', 'is_approved', 'is_checked']

    def __init__(self, *args, **kwargs):
        super(ApplicationForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})


class LectureApplicationForm(ModelForm):
    class Meta:
        model = Application
        fields = ['is_approved']

    def __init__(self, *args, **kwargs):
        super(LectureApplicationForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})


class AddApplicationForm(ModelForm):
    class Meta:
        model = Application
        fields = '__all__'
        exclude = ['is_checked']

    def __init__(self, *args, **kwargs):
        super(AddApplicationForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})
