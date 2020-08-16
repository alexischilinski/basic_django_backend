from django.shortcuts import render
from rest_framework import viewsets, permissions
from .serializers import ReviewSerializer, RegisterSerializer
from .models import Review
from rest_framework.response import Response
from django.contrib.auth.models import User

# Create your views here.

class ReviewViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny]
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class RegisterView(viewsets.ModelViewSet):

    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        if user:
            return Response({
            "user": UserSerializer(user,
                context=self.get_serializer_context()).data
            })
        return Response