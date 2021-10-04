
from django.urls import path, include
from . import views


from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('users/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('users/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('users/', views.getUsers),
    path('user/<str:pk>/', views.getUser),

    path('students/', views.getStudents),
    path('student/<str:pk>/', views.getStudent),

    path('lectures/', views.getLectures),
    path('lecture/<str:pk>/', views.getLecture),

    path('', views.getRoutes),
    path('projects/', views.getProjects),
    path('project/<str:pk>/', views.getProject),

]
