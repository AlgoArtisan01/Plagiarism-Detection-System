from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name='plagiarism-check-mainpage'),
    path('test/', views.test,name='Test'),
    path('filetest/', views.filetest,name='filetest')
]
