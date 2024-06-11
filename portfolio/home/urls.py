
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name="home"),
    path('send',views.send,name="send"),
]
