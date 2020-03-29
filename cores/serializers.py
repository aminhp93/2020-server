from rest_framework import serializers

from .models import Config

class ConfigSerialzier(serializers.ModelSerializer):
    class Meta:
        model = Config
        fields = '__all__'
