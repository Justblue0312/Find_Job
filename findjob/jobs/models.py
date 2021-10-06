from typing import Tuple
from users.models import Lecture, Student
from django.db import models
import uuid

# Create your models here.


class JobPost(models.Model):
    title = models.CharField(max_length=255)
    job_image = models.ImageField(
        null=True, blank=True, upload_to='jobs/', default="profiles/user-default.png")
    author = models.ForeignKey(
        Lecture, null=True, blank=True, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=255, null=True, blank=True)
    company_location = models.CharField(max_length=255, null=True, blank=True)
    company_phone = models.CharField(max_length=255, null=True, blank=True)
    company_email = models.CharField(max_length=255, null=True, blank=True)
    jobs_desc = models.TextField(max_length=10000, null=True, blank=True)
    jobs_tags = models.ManyToManyField(
        'Need', blank=True, related_name='needs')
    jobs_required = models.IntegerField(null=True, blank=True, default=1)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    archived = models.BooleanField(default=False, editable=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-timestamp", "-updated"]


class Need(models.Model):
    name = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return self.name


class Application(models.Model):
    jobpost = models.ForeignKey(
        JobPost, on_delete=models.CASCADE, null=True, blank=True)
    applicant = models.ForeignKey(
        Student, on_delete=models.CASCADE, null=True, blank=True)
    is_approved = models.BooleanField(default=False)
    is_checked = models.ForeignKey(
        Lecture, on_delete=models.SET_NULL, null=True, blank=True)
    description = models.TextField(blank=True, null=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    date_applied = models.DateTimeField(auto_now=False, auto_now_add=True)
    archived = models.BooleanField(default=False, editable=False)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return str(self.jobpost)

    class Meta:
        ordering = ["-date_applied", "-updated"]
