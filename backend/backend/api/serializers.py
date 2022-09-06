from rest_framework import serializers
from themes.models import Theme
from questions.models import Question , Answer
class ThemeSerializers(serializers.ModelSerializer):
    class Meta:
        model = Theme
        fields = '__all__'
class AnswerSerializers(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = '__all__'
class QuestionSerializers(serializers.ModelSerializer):
    right_answer = AnswerSerializers()
    wrong_answer = AnswerSerializers()   
    class Meta:
        model = Question
        fields = '__all__'
