from django.urls import path
from . import views

urlpatterns = [
    path('home/',views.home,name="home"),
    path('croppredict/',views.cropprediction,name="cropprediction"),
    path('fertiliser/',views.fertiliser,name="fertiliser"),
    path('signup/',views.signup,name='signup'),
    path('',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
    path('view/<int:id>/',views.viewtask,name="viewtask"),
    path('remove/<int:id>/',views.removetask,name="removetask"),
    path('update/<int:id>/',views.updatetask,name="updatetask"),
    path('add/',views.addtask,name="addtask"),
    path('tasks/',views.tasks,name="tasks")
]