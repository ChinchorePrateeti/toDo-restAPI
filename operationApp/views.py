from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import toDo
from .serializers import toDoSerializer



@api_view(['POST'])
def taskUpdate(request, pk):
    task = toDo.objects.get(id = pk)
    serializer = toDoSerializer(instance=task, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['GET'])
def viewList(request):
    response = {'status':200}
    todoList = toDo.objects.all()
    serializeList = toDoSerializer(todoList, many = True)
    response['data'] = serializeList.data
    return Response(response)

@api_view(['POST'])
def addToList(request):
    response = {'status' : 200}
    data = request.data
    serializeData = toDoSerializer(data = data)
    if serializeData.is_valid():
        serializeData.save()
        response['data'] = serializeData.data
        return Response(response)
    return Response(serializeData.errors)

@api_view(['DELETE'])
def taskDelete(request, pk):
    task = toDo.objects.get(id = pk)
    task.delete()
    return Response("Taks deleted successfully.")