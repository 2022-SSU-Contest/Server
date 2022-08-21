from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Video
from .serializers import VideosSerializer
from rest_framework import permissions



@api_view(['GET'])
def getVideoAPI(request): 
    words = request.GET['words']
    print("입력 : " + words)
    # words -> 형태소 분석
    # videos = Video.objects.all()
    words = words.split(',')
    print(words)
    for w in words:
        videos = Video.objects.filter(word=w)
        serializer = VideosSerializer(videos,many=True)
        Response(serializer.data)
        # print(serializer)
        # print("url : " + serializer.url)


    return Response(serializer.data)

