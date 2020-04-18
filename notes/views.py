from django.shortcuts import render
from django.shortcuts import get_object_or_404

# Create your views here.
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response

from notes.models import Note

from notes.serializers import NoteSerializer


# Create your views here.
class NoteViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Note.objects.all()
        serializer = NoteSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        data = request.data
        serializer = NoteSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        note = get_object_or_404(Note, pk=pk)
        serializer = NoteSerializer(note)
        return Response(serializer.data)

    def update(self, request, pk=None):
        pass

    def partial_update(self, request, pk=None):
        note = get_object_or_404(Note, pk=pk)
        serializer = NoteSerializer(note, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        note = get_object_or_404(Note, pk=pk)
        note.delete()
        return Response({})