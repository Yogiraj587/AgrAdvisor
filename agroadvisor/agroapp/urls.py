from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('croppredict/',views.cropprediction,name="cropprediction"),
    path('fertiliser/',views.fertiliser,name="fertiliser")
]