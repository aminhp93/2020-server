from django.shortcuts import render
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView
)

from rest_framework.response import Response
from rest_framework import status
from django.core.management import call_command


from .serializers import ConfigSerialzier

from .models import Config

# Create your views here.
class ConfigListAPIView(ListAPIView):
    serializer_class = ConfigSerialzier
    # queryset = Config.objects.all()

    def get(self, request, *args, **kwargs):
        key = request.GET.get('key')
        filteredConfig = Config.objects.filter(key=key)
        if filteredConfig.count() != 1:
            return Response({}, status=status.HTTP_200_OK)
        serialzier = ConfigSerialzier(filteredConfig[0])
        return Response(serialzier.data, status=status.HTTP_200_OK)


class ConfigCreateAPIView(CreateAPIView):
    serializer_class = ConfigSerialzier
    queryset = Config.objects.all()


class ConfigRetrieveAPIView(RetrieveAPIView):
    serializer_class = ConfigSerialzier
    queryset = Config.objects.all()


class ConfigUpdateAPIView(UpdateAPIView):
    serializer_class = ConfigSerialzier
    queryset = Config.objects.all()

    def perform_update(self, serialzier):
        serialzier.save()
        call_command('update_latest_stock')        


class ConfigDestroyAPIView(DestroyAPIView):
    serializer_class = ConfigSerialzier
    queryset = Config.objects.all()
