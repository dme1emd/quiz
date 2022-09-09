from .serializers import *
from rest_framework import response , decorators
from questions.models import * 
from themes.models import *
# Create your views here.
@decorators.api_view(['GET'])
def themes_api_view(request):
    qs = Theme.objects.all()
    serializer = ThemeSerializers(qs , many = True ,context={'request': request}).data
    return response.Response(serializer , status=200)
@decorators.api_view(['GET'])
def questions_api_view(request , pk):
    diff = request.query_params.get('difficulty')
    print(diff)
    theme = Theme.objects.get(pk = pk )
    qs = Question.objects.filter(theme = theme , difficulty=diff)
    serializer = QuestionSerializers(qs , many = True,context={'request': request}).data
    return response.Response(serializer , status=200)