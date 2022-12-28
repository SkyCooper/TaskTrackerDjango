from django.urls import path,include
# from .views import TodoList, TodoDetail
# from .views import TodoGV, TodoDetailGV

from .views import TodoMVS
from rest_framework import routers

router = routers.DefaultRouter()
router.register('todo', TodoMVS)

urlpatterns = [
    
    # path('', TodoList),
    # path('detail/<int:pk>', TodoDetail),
    
    # path('', TodoGV.as_view()),
    # path('detail/<int:pk>', TodoDetailGV.as_view()),
    
    # path('', include(router.urls)),
]

urlpatterns += router.urls