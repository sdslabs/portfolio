from django.urls import path

from . import views

urlpatterns = [
    path('', views.get_timeline, name='get_timeline'),
]
