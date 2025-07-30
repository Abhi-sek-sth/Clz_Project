from django.urls import path
from Online_Food import views

urlpatterns = [
    path("", views.main, name="main"),
    
]