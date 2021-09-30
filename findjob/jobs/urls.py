from django.urls import path
from . import views

urlpatterns = [
    path('jobs/', views.jobs, name='jobs'),
    path('job/<str:pk>/', views.job, name='job'),

    path('l_profile/', views.lectureProfile, name='l_profile'),
    path('editl_profile/', views.editLProfile, name='editLProfile'),

    path('addjob/', views.addJob, name='addjob'),
    path('updatejob/<str:pk>/', views.updateJob, name='updatejob'),
    path('deletejob/<str:pk>/', views.deleteJob, name='deletejob'),

    path('approvedJobs/', views.approvedJobs, name='approvedJobs'),
    path('approvedJob/<str:pk>', views.approvedJob, name='approvedJob'),

    path('addapp/', views.addApp, name='addapp'),
]
