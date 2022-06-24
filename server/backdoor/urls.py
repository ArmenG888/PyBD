from django.urls import path
from . import views 

urlpatterns = [
    path('', views.home, name="home"),
    path('pc/<pc_id>/', views.computer_detail, name="computer-detail"),
    path("ajax/<pk>", views.ajax, name="ajax"),
    path("pc_ajax/<pk>", views.check_pc_online, name="ajax-pc"),
    path("clean/<pk>", views.clean, name="clean"),
    path("files/", views.screenshot, name="screenshot")
]