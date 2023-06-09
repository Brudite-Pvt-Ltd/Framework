from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Emp_system
from .serializers import EmpSerializer
from rest_framework import status


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def Emp_API(request):
    if request.method == 'GET':
        id = request.data.get('id')
        if id is not None:
            emp = Emp_system.objects.get(id=id)
            serial = EmpSerializer(emp)
            return Response(serial.data)
        else:
            emp = Emp_system.objects.all()
            serial = EmpSerializer(emp, many=True)
            return Response(serial.data)

    elif request.method == 'POST':
        serial = EmpSerializer(data=request.data)
        if serial.is_valid:
            serial.save()
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PUT':
        id = request.data.get('id')
        emp = Emp_system.objects.get(pk=id)
        serial = EmpSerializer(emp, data=request.data, partial=True)
        if serial.is_valid:
            serial.save()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        id = request.data.get('id')
        emp = Emp_system.objects.get(pk=id)
        emp.delete()
        return Response(status=status.HTTP_202_ACCEPTED)
