from rest_framework import serializers
from .models import Dep_system


class DepSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dep_system
        fields = ['DepName', 'Department_Head']
        # We can also do this by fields= '__all__'
