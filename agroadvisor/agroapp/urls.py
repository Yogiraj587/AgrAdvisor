from django.urls import path
from . import views

urlpatterns = [
    path('home/',views.home,name="home"),
    path('croppredict/',views.cropprediction,name="cropprediction"),
    path('fertiliser/',views.fertiliser,name="fertiliser"),
    path('signup/',views.signup,name='signup'),
    path('',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
    path('delete-task/<str:name>/', views.Delete, name='delete'),
    path('update/<str:name>/', views.Update, name='update'),
    path('tasks/',views.tasks,name="tasks")
]