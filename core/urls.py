from django.urls import path , include
from rest_framework.routers import DefaultRouter
from .views import NoteViewSet, RegisterView

#creating a router and registering our viewset with it . 
router= DefaultRouter()


#First argument 'notes' is the url name and will start with /notes/
router.register(r'notes',NoteViewSet,basename= 'note')

#The API URLs are now determined aitomatically by the router. 
urlpatterns= [
    path('', include(router.urls)),
    path('register/', RegisterView.as_view(), name= 'register')
]


#WHAT WHAT I DID TODAY :
#1.  I made the JWT authentication and authorization work . 
#2.  I created the NoteViewSet and RegisterView
#3. I created the serializers for Note and Register
#4. I created the urls for NoteViewSet and RegisterView
#5. I created the models for Note and User
#6. I created api for users to register and login . 
#7. I created tokens for authentication and authorization. 
#8. I learned about the router and how it works.abs
#9. I learn about acess token and refresh token . 
#10. I learned the diff between modelviewset and generics 
# ModelViewSet-> whole CRUD. 
# Generics-> only specific methods. 
