from rest_framework import serializers
from user.models import User


class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)
    name = serializers.CharField(required=False)
    weight = serializers.FloatField(required=False)
    height = serializers.FloatField(required=False)
    preferences = serializers.CharField(required=False)
    diseases = serializers.CharField(required=False)

    class Meta:
        model = User
        fields = "__all__"

