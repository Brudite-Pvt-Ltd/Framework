# Importing necessary dependencies and modules for the DRF API view

from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Dep_system
from .serializers import DepSerializer
from rest_framework import status
from Emp.serializers import EmpSerializer
from collections import OrderedDict
import json
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
        # Retreive all employees
        employees = dep.emp_system_set.all()
        serial = EmpSerializer(employees, many=True)
        data = serial.data
        salaries = [item['Salary'] for item in data]
        sum_of_salaries = sum(salaries)
        return Response(sum_of_salaries, status=status.HTTP_202_ACCEPTED)

        """
        #  This is another method to get sum of all employees salary in a deaprtment by 
        # ordering all salary and then making a empty list and storing salaries of all employee
        # in dict format and then again convert it into the list format which conatains salary only in salaries 
        # attribute
        
        employees = dep.emp_system_set.order_by('Salary')
        Result = []
        for i in employees:
            data = {
                "Salary": i.Salary
            }
            Result.append(data)
        salaries = []
        for j in range(len(Result)):
            salaries.append(Result[j]['Salary'])
        sum_salary = sum(salaries)
        return Response(sum_salary, status=status.HTTP_202_ACCEPTED)
        """


""" This function is defined to get the top 3 salaries in a particular department"""


@api_view(['GET'])
def Top3Salary(request, DN):
    if request.method == 'GET':
        # Retrieve the Dep_system object based on the provided DepName
        dep = Dep_system.objects.get(DepName=DN)
        # Retrieve all associated emp_system objects for the Dep_system object in order of top 3 salary
        a = dep.emp_system_set.order_by('-Salary')[:3]
        serial = EmpSerializer(a, many=True)
        return Response(serial.data, status=status.HTTP_202_ACCEPTED)


""" This function is defined to get the top 3 salaries in a particular department and the Name of employee and its Salary"""


@api_view(['GET'])
def Top3Salarya(request, DN):
    if request.method == 'GET':
        # Retrieve the Dep_system object based on the provided DepName
        dep = Dep_system.objects.get(DepName=DN)
        # Retrieve the top 3 emp_system objects for the Dep_system object in order of top salary
        employees = dep.emp_system_set.order_by('-Salary')[:3]
        result = []
        for i in employees:
            print(i)
            data = {
                'Name': i.Name,
                'Salary': i.Salary
            }
            result.append(data)

        return Response(result, status=status.HTTP_202_ACCEPTED)
