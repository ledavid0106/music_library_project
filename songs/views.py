from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Song
from .serializers import SongSerializer
from rest_framework import status

@api_view(['GET', 'POST'])
def songs_list(request):
    if request.method == "GET":
        songs = Song.objects.all()
        serializer = SongSerializer(songs, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = SongSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def song_detail(request, pk):
    song = get_object_or_404(Song, pk=pk)
    if request.method =='GET':
    #New shortcut code that does the same thing
        serializer = SongSerializer(song)
        return Response(serializer.data)
    elif request.method =='PUT':
        serializer = SongSerializer(song, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    #The below is the original code
    # try:
    #     song = Song.objects.get(pk=pk)
    #     serializer = SongSerializer(song)
    #     return Response(serializer.data)
    # except Song.DoesNotExist:
    #     return Response(status=status.HTTP_404_NOT_FOUND)
    elif request.method == 'DELETE':
        song.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

        