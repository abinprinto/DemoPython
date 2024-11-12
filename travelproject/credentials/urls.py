from django.urls import path

from credentials import views

urlpatterns = [
    path('register',views.register,name='register'),]