from django.urls import path, include
from lyrics import views

urlpatterns = [
    path('lyrics/', views.signup)
]