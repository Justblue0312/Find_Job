from django.contrib import admin
from .models import Skill, User, Student, Lecture

# Register your models here.
admin.site.register(User)
admin.site.register(Student)
admin.site.register(Lecture)
admin.site.register(Skill)
