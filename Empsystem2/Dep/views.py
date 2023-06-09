from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Dep_system
from .serializers import DepSerializer
from rest_framework import status


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def Dep_API(request):
    if request.method == 'GET':
        id = request.data.get('id')
        if id is not None:
            dep = Dep_system.objects.get(id=id)
            serial = DepSerializer(dep)
            return Response(serial.data)
        else:
            dep = Dep_system.objects.all()
            serial = DepSerializer(dep, many=True)
            return Response(serial.data)

    elif request.method == 'POST':
        serial = DepSerializer(data=request.data)
        if serial.is_valid():
            serial.save()
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PUT':
        id = request.data.get('id')
        dep = Dep_system.objects.get(pk=id)
        serial = DepSerializer(dep, data=request.data, partial=True)
        if serial.is_valid():
            serial.save()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        id = request.data.get('id')
        dep = Dep_system.objects.get(pk=id)
        dep.delete()
        return Response(status=status.HTTP_202_ACCEPTED)
