from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Note

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User #Creating a user model from Django
        fields = ["id", "username", "password"] #Fields of the user class
        extra_kwargs = {"password": {"write_only": True}} #Makes password write-only so that no one can read it.

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data) #Creates a new user using the data given. This data is already checked by the Serializer.
        return user

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ["id", "title", "content", "created_at", "author"]
        extra_kwargs = {"author": {"read_only": True}}