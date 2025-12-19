from rest_framework import serializers 
from django.contrib.auth.models import User
from .models import Note

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        #We are using id here, where did this id came from? Django automatically creates id when creating a model . 

        fields= ['id', 'title', 'body', 'created_at']
        

class RegisterSerializer(serializers.ModelSerializer):
    # hiding the password in response
    password= serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields= ['username', 'email', 'password']

    def create(self,validated_data):
        # This creates the user and hasesh the password automatically. 
        user = User.objects.create_user(
            username= validated_data['username'],
            email= validated_data['email'],
            password= validated_data['password']
        )
        return user