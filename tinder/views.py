from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from .models import User
from .serializers import ApiView

# Create your views here.
def home(request):
    return HttpResponse('Hey')

class ApisView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = ApiView


class AddView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = ApiView


class UpdateView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = ApiView

class DeleteView(generics.DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = ApiView

