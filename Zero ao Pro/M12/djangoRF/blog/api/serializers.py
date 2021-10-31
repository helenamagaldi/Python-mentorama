from django.contrib.auth.models import User
from rest_framework import serializers
from api.models import Post


class UserSerializer(serializers.ModelSerializer):
    post = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = User
        fields = ["id", "username", "first_name", "last_name"]

class PostSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.username")

    class Meta:
        model = Post
        fields = ["id", "username", "owner"]

