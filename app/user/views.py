"""
Views for ther user API.
"""
from rest_framework import generics

from user.serializers import UserSerializer


class CreateUserAPIView(generics.CreateAPIView):
    """Create a new user in the system."""
    serializer_class = UserSerializer
