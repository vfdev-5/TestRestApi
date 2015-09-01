from django.contrib.auth.models import User

from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    images = serializers.StringRelatedField(many=True)

    class Meta:
        model = User
        # fields = ('username', 'email', 'images')

