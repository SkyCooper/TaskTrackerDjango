from django.urls import path,include
from .views import TodoList, TodoDetail

urlpatterns = [
    path('', TodoList),
    path('detail/<int:pk>', TodoDetail),
]