from tkinter.messagebox import QUESTION
from django.shortcuts import render
from .serializers import *
from rest_framework import response , decorators
from questions.models import * 
from themes.models import *
# Create your views here.
@decorators.api_view(['GET'])
def themes_api_view(request):
    qs = Theme.objects.all()
    serializer = ThemeSerializers(qs , many = True).data
    return response.Response(serializer , status=200)
@decorators.api_view(['GET'])
def questions_api_view(request , pk):
    theme = Theme.objects.get(pk = pk )
    qs = Question.objects.filter(theme = theme)
    serializer = QuestionSerializers(qs , many = True).data
    return response.Response(serializer , status=200)