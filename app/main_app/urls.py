from django.conf.urls import url
from app.main_app import views

urlpatterns = [
    url('home', views.health),
]
