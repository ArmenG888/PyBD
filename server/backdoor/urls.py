from django.urls import path
from . import views 

urlpatterns = [
    path('', views.home, name="home"),
    path('<pc_id>/', views.computer_detail, name="computer-detail"),
    path("ajax/<pk>", views.ajax, name="ajax")
]