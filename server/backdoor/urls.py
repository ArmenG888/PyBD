from django.urls import path
from . import views 

urlpatterns = [
    path('', views.home, name="home"),
    path('ajax', views.live_output_data, name="ajax")
]