from django.shortcuts import render
from rest_framework import viewsets
# Create your views here.
from .models import Language
from .serializers import LanguageSerializer


class LanguageView(viewsets.ModelViewSet):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer