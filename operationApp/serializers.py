from rest_framework import serializers
from .models import toDo

class toDoSerializer(serializers.ModelSerializer):
    class Meta:
        model = toDo
        fields = '__all__'