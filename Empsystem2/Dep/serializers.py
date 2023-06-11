# Importing necessary dependencies and modules
from rest_framework import serializers
from .models import Dep_system

# creating ModelSerializer


class DepSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dep_system
        fields = ['DepName', 'Department_Head']
        # We can also do this by fields= '__all__'
