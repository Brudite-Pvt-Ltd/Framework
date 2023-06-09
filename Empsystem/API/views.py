from django.shortcuts import render
from .models import Emp_system, Dep_system
import io
from rest_framework.parsers import JSONParser
from .serializers import EmpSerializer, DepSerializer, Empserial
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status


@csrf_exempt
def Emp_API(request, pk):
    if request.method == 'GET':
        if pk is not 0:
            emp = Emp_system.objects.get(pk=pk)
            serializer = EmpSerializer(emp)
            json_data2 = JSONRenderer().render(serializer.data)
            return HttpResponse(json_data2, content_type='application/json')
        else:
            emp = Emp_system.objects.all()
            serializer = EmpSerializer(emp, many=True)
            json_data = JSONRenderer().render(serializer.data)
            return HttpResponse(json_data, content_type='application/json')

    elif request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pydata = JSONParser().parse(stream)
        serializer = EmpSerializer(data=pydata)
        if serializer.is_valid():
            serializer.save()
            resp = {'msg': 'Data created'}
            json_data = JSONRenderer().render(resp)
            return HttpResponse(json_data, content_type='application/json')
        return HttpResponse(status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        if pk is not 0:
            emp = Emp_system.objects.get(pk=pk)
            emp.delete()
            return HttpResponse(status=status.HTTP_204_NO_CONTENT)
        else:
            emp = Emp_system.objects.all()
            emp.delete()
            return HttpResponse(status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pydata = JSONParser().parse(stream)
        emp = Emp_system.objects.get(pk=pk)
        serializer = EmpSerializer(emp, data=pydata, partial=True)
        if serializer.is_valid():
            serializer.save()
            return HttpResponse(status=status.HTTP_204_NO_CONTENT)
        return HttpResponse(status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
def Emp_API1(request):
    if request.method == 'POST':
        json_data = request.body
        # stream = io.BytesIO(json_data)
        # pydata = JSONParser().parse(stream)
        serial = Empserial(data=json_data)
        print(serial)
        if serial.is_valid():
            serial.save()
            resp = {'msg': 'Data created'}
            json_data = JSONRenderer().render(resp)
            return HttpResponse(json_data, content_type='application/json')
        return HttpResponse(status=status.HTTP_400_BAD_REQUEST)

# View Fucntion for the Department API


@csrf_exempt
def Dep_API(request, pk):
    # Writing for the Create
    if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pydata = JSONParser().parse(stream)
        serial = DepSerializer(data=pydata)
        if serial.is_valid():
            serial.save()
            # resp = {'msg': 'Data created'}
            # json_data = JSONRenderer().render(resp)
            return HttpResponse(serial, content_type='application/json')
        return HttpResponse("Invalid")

    # Writing for the Get method
    elif request.method == 'GET':
        if pk is not 0:
            dep = Dep_system.objects.get(pk=pk)
            serializer = DepSerializer(dep)
            json_data = JSONRenderer().render(serializer.data)
            return HttpResponse(json_data, content_type='appliation/json')
        else:
            dep = Dep_system.objects.all()
            serializer = DepSerializer(dep, many=True)
            json_data = JSONRenderer().render(serializer.data)
            return HttpResponse(json_data, content_type='appliation/json')

    # Writing for the PUT method
    elif request.method == 'PUT':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pydata = JSONParser().parse(stream)
        dep = Dep_system.objects.get(pk=pk)
        serializer = DepSerializer(dep, data=pydata, partial=True)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({"done": 200})
        else:
            return JsonResponse(status.HTTP_400_BAD_REQUEST)

    # Writing for the Delete request
    elif request.method == 'DELETE':
        if pk is not 0:
            dep = Dep_system.objects.get(pk=pk)
            dep.delete()
            return HttpResponse(status=status.HTTP_204_NO_CONTENT)
        else:
            dep = Dep_system.objects.all()
            dep.delete()
            return HttpResponse(status=status.HTTP_204_NO_CONTENT)
