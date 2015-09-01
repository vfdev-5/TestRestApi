
from rest_framework import serializers

from RestApi.models import Photo

class PhotoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Photo
