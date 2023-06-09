from django.urls import path
from . import views

urlpatterns = [
    path('', views.viewList),
    path('add/', views.addToList),
    path('task-update/<str:pk>/', views.taskUpdate, name="task-update"),
    path('task-delete/<str:pk>/', views.taskDelete, name="task-delete"),
]