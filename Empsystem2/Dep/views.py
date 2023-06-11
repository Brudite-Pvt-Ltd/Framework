# Importing necessary dependencies and modules for the Django REST framework API view

from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Dep_system
from .serializers import DepSerializer
from rest_framework import status
from Emp.serializers import EmpSerializer
from collections import OrderedDict

# Create a API View for Retrieving the Data of Department


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def Dep_API(request):
    if request.method == 'GET':
        id = request.data.get('id')
        if id is not None:
            # Retrieve a specific Dep_system object based on the provided ID
            dep = Dep_system.objects.get(id=id)
            serial = DepSerializer(dep)
            return Response(serial.data)
        else:
            # Retrieve all Dep_system objects
            dep = Dep_system.objects.all()
            serial = DepSerializer(dep, many=True)
            return Response(serial.data)

    elif request.method == 'POST':
        # Create a new Dep_system object using the provided data
        serial = DepSerializer(data=request.data)
        if serial.is_valid():
            serial.save()
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PUT':
        id = request.data.get('id')
        # Retrieve an existing Dep_system object based on the provided ID
        dep = Dep_system.objects.get(pk=id)
        # Update the Dep_system object with the provided data
        serial = DepSerializer(dep, data=request.data, partial=True)
        if serial.is_valid():
            serial.save()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        id = request.data.get('id')
        # Retrieve an existing Dep_system object based on the provided ID
        dep = Dep_system.objects.get(pk=id)
        # Delete the Dep_system object
        dep.delete()
        return Response(status=status.HTTP_202_ACCEPTED)


@api_view(['GET'])
def AllEmp(request, DN):
    if request.method == 'GET':
        # Retrieve the Dep_system object based on the provided DepName
        dep = Dep_system.objects.get(DepName=DN)
        # Retrieve all associated emp_system objects for the Dep_system object
        a = dep.emp_system_set.all()
        serial = EmpSerializer(a, many=True)
        return Response(serial.data, status=status.HTTP_202_ACCEPTED)


@api_view(['GET'])
def AllEmpSalary(request, DN):
    if request.method == 'GET':
        # Retrieve the Dep_system object based on the provided DepName
        dep = Dep_system.objects.get(DepName=DN)
        # Retrieve all associated emp_system objects for the Dep_system object
        a = dep.emp_system_set.all()
        serial = EmpSerializer(a, many=True)
        # Convert the serialized data to a Python list
        python_list = list(serial.data.items())
        print(python_list)
        return Response(serial.data, status=status.HTTP_202_ACCEPTED)

# b = (len(serial.data))
        # c = serial.data
        # print(type(c))
        # d = []
        # for item in serial.data:
        #     d.append(item)

        # li = []
        # for i in d[0]:
        #     li.append(i)
