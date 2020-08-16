from rest_framework import serializers
from .models import Review
from django.contrib.auth.models import User

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

class RegisterSerializer(serializers.ModelSerializer):
   class Meta:
      model = User
      fields = ('id', 'username', 'email', 'password')
      extra_kwargs = {'password' : {'write_only': True}}
   def create(self, validated_data):
      user = User.objects.create_user(validated_data['username'],
         validated_data['email'], validated_data['password']
      )
      return user