from django.urls import path

from polls import views

urlpatterns = [
    path("", views.index, name="polls"),
    path("about", views.about, name="about"),
    path("services", views.services, name="services"),
    path ("contact", views.contact,name='contact'),
   
]