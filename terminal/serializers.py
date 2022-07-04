from rest_framework import serializers
from .models import Command_Bank

class Command_serializer(serializers.ModelSerializer):

    class Meta:
        model = Command_Bank
        fields = ["title","command","framework",]