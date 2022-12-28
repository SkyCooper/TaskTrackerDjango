from django.shortcuts import render, get_object_or_404

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet

from .models import Todo
from .serializer import TodoSerializer

# Create your views here.

@api_view(['GET', 'POST'])
def TodoList(request):
  if request.method == 'GET':
    todos = Todo.objects.all()
    serializer = TodoSerializer(todos, many=True)
    return Response(serializer.data)
  
  if request.method == 'POST':
    serializer = TodoSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def TodoDetail(request, pk):
  todo = get_object_or_404(Todo, id=pk)
  
  if request.method == 'GET':
    serializer = TodoSerializer(todo)
    return Response(serializer.data)
  
  if request.method == 'PUT':
    serializer = TodoSerializer(data=request.data, instance=todo)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
  if request.method == 'DELETE':
    todo.delete()
    return Response({"message" : "Todo deleted.."})

  
class TodoGV(ListCreateAPIView):
  queryset = Todo.objects.all()
  serializer_class = TodoSerializer
  
class TodoDetailGV(RetrieveUpdateDestroyAPIView):
  queryset = Todo.objects.all()
  serializer_class = TodoSerializer
    
class TodoMVS(ModelViewSet):
  queryset = Todo.objects.all()
  serializer_class = TodoSerializer  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  