from django.core import serializers
from rest_framework import serializers
from .models import Video

class VideosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        # fields=('url',)
        fields = ('word','url')
    # id = serializers.IntegerField()
    word = serializers.CharField()
    url = serializers.CharField()