from django.urls import path
from . import views

urlpatterns = [
    path('', views.choose,name="choose"),
    path('show_data/', views.show_data,name="show_data"),

]
