from rest_framework import serializers
from .models import QuizArchive

# serializer to randomly query n number of quiz questions


class getQuizQuestionsSerializers(serializers.ModelSerializer):
    class Meta:
        model = QuizArchive
        fields = '__all__'
        
        # ['question', 'option_one', 'option_two', 'option_three', 'option_four']
