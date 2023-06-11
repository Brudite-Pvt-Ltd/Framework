# Importing necessary dependencies and modules for the DRF API view
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Emp_system
from .serializers import EmpSerializer
from rest_framework import status
from Dep.models import Dep_system

# Create a API View for Retrieving the Data of Employment


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def Emp_API(request):
    if request.method == 'GET':
        id = request.data.get('id')
        if id is not None:
            # Retrieve a specific Emp_system object based on the provided ID
            emp = Emp_system.objects.get(id=id)
            serial = EmpSerializer(emp)
            return Response(serial.data)
        else:
            # Retrieve all Emp_system objects
            emp = Emp_system.objects.all()
            serial = EmpSerializer(emp, many=True)
            return Response(serial.data)

    elif request.method == 'POST':
        # Create a new Emp_system object using the provided data
        serial = EmpSerializer(data=request.data)
        if serial.is_valid():
            serial.save()
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'PUT':
        id = request.data.get('id')
        # Retrieve an existing Emp_system object based on the provided ID
        emp = Emp_system.objects.get(pk=id)
        # Update the Emp_system object with the provided data
        serial = EmpSerializer(emp, data=request.data, partial=True)
        if serial.is_valid():
            serial.save()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        id = request.data.get('id')
        # Retrieve an existing Emp_system object based on the provided ID
        emp = Emp_system.objects.get(pk=id)
        # Delete the Emp_system object
        emp.delete()
        return Response(status=status.HTTP_202_ACCEPTED)


# @api_view(['GET', 'POST', 'PUT', 'DELETE'])
# def AllEmp(request):
#     if request.method == 'GET':
#         DN = request.data.get('DN')
#         dep = Dep_system.objects.get(DepName=DN)
#         a = dep.emp_system_set.all()
#         serial = EmpSerializer(a)
#         return Response(serial.data, status=status.HTTP_202_ACCEPTED)
