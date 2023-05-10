from django.urls import path
from tours import views

urlpatterns = [
    path('tours/', views.TourList.as_view()),
    path('tours/<int:pk>/', views.TourDetail.as_view()),
]
