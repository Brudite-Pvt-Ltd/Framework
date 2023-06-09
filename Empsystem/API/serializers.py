from rest_framework import serializers
from .models import Emp_system, Dep_system


class EmpSerializer(serializers.Serializer):
    # id = serializers.IntegerField()
    Name = serializers.CharField(max_length=80)
    Salary = serializers.FloatField()
    Description = serializers.CharField(max_length=80)
    Designation = serializers.CharField(max_length=80)
    Manager = serializers.CharField(max_length=70)
    Dep_Name = serializers.CharField(max_length=80)

    def create(self, validated_data):
        return Emp_system.objects.create(**validated_data)

    def update(self, instance, validated_data):
        # instance.id = validated_data.get('id', instance.id)
        instance.Name = validated_data.get('Name', instance.Name)
        instance.Salary = validated_data.get('Salary', instance.Salary)
        instance.Description = validated_data.get(
            'Description', instance.Description)
        instance.Designation = validated_data.get(
            'Designation', instance.Designation)
        instance.Manager = validated_data.get('Manager', instance.Manager)
        instance.Dep_Name = validated_data.get(
            'Dep_Name', instance.Dep_Name)
        instance.save()

        return instance


# department Serializer
class DepSerializer(serializers.Serializer):
    Dep_Name = serializers.CharField(max_length=80)
    Department_Head = serializers.CharField(max_length=80)

    def create(self, validated_data):
        return Dep_system.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.Dep_Name = validated_data.get('Name', instance.Dep_Name)
        instance.Department_Head = validated_data.get(
            'Department_Head', instance.Department_Head)
        instance.save()

        return instance


class Empserial(serializers.ModelSerializer):

    class Meta:
        model = Emp_system
        fields = '__all__'
