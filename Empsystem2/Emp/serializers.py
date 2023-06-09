from rest_framework import serializers
from .models import Emp_system


class EmpSerializer(serializers.ModelSerializer):
    class Meta:
        model = Emp_system
        fields = '__all__'
        # We can also do this by fields= '__all__'
