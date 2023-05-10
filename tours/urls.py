from django.urls import path
from tours import views

urlpatterns = [
    path('tours/', views.TourList.as_view()),
]
