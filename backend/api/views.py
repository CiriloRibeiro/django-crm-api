from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics
from .models import Lead
from .serializers import LeadSerializer, UserSerializer

# Create your views here.
class LeadListCreateView(generics.ListCreateAPIView):
    serializer_class = LeadSerializer
    queryset = Lead.objects.all()
    
class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
class LeadRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = LeadSerializer
    queryset = Lead.objects.all()