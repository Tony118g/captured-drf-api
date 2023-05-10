from django.urls import path
from attendances import views

urlpatterns = [
    path('attendances/', views.AttendanceList.as_view()),
]
