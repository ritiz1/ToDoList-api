from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from .models import Note 
from .serializers import NoteSerializer
from rest_framework import generics
from rest_framework.permissions import AllowAny
from .serializers import RegisterSerializer
from django.contrib.auth.models import User

class NoteViewSet(viewsets.ModelViewSet):
    #This is the translator. It translates the json to python.
    serializer_class= NoteSerializer

    #THe Security GUard
    #This ensures only loggedin users can access this EndPoints;
    permission_classes= [IsAuthenticated]

    #3. The QuerySet (THe filter)
    #We don't return Notes.objects.all() here because that would show everbodys dataa.
    #We override this method to only return notes belonging to the current users.abs
    def get_queryset(self):
        return Note.objects.filter(owner= self.request.user)
    

    #4. The Auto-Owner
    #When a user Create(POST) a note, they dont send their own ID. 
    #We automatically inject their ID here. 
    def perform_create(self, serializer):
        serializer.save(owner= self.request.user)


class RegisterView(generics.CreateAPIView):
    queryset= User.objects.all()
    permission_classes= [AllowAny]
    serializer_class= RegisterSerializer

# Create your views here.
