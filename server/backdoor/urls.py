from django.urls import path
from . import views 

urlpatterns = [
    path('', views.home, name="home"),
    path('pc/<pc_id>/', views.computer_detail, name="computer-detail"),


    # api
    path("api/commands/<pk>", views.commands),
    path("api/output/<pk>/<command_id>", views.output),
    path("api/ping/<pk>", views.ping),
    path("api/get_id/<pk>", views.get_id),
    path("api/files/", views.screenshot),

    # js
    path("ajax/online/<pk>", views.ajax, name="ajax"),
    path("ajax/pc/<pk>", views.check_pc_online, name="ajax-pc"),
    path("ajax/clean/<pk>", views.clean, name="clean"),
    
]