from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Video
from .serializers import VideosSerializer
from rest_framework import permissions
from django.http import JsonResponse
from konlpy.tag import Komoran
komoran = Komoran()

@api_view(['GET'])
def getVideoAPI(request): 
    sentence = request.GET['words']
    # print("입력 : " + words)
    # words -> 형태소 분석
    # videos = Video.objects.all()
    morpheme = komoran.pos(sentence)
    words = list(map(lambda x : x[0],morpheme))
    print(words)
    res=[]
    for w in words:
        videos = Video.objects.filter(word=w)
        serializer = VideosSerializer(videos,many=True)
        for s in serializer.data:
            res.append(dict(s).get('url'))
    jsonData = JsonResponse(res, safe=False, json_dumps_params={'ensure_ascii': False})
    return jsonData

