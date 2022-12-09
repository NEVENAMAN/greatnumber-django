from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('testNumber',views.test),
    path('win_Number',views.win),
]