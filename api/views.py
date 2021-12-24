from django.shortcuts import render
import random
from .models import QuizArchive

from .serializers import getQuizQuestionsSerializers

from rest_framework import status, generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response


# Create your views here.
@api_view(['GET'])
def quiz_questions(request):

    query = request.data or request.query_params

    try:
        # number of random question that should be queried
        num_random = query['rand']
    except Exception as e:
        pass

    # query all the quiz questions in 'QuizArchive' Database
    queryset = QuizArchive.objects.all().order_by('-id')
    get_all_ids = list(queryset.values_list('id', flat=True))
    print(get_all_ids)
    try:
        # this randomly picks n number of quiz questions id
        random_ids = random.sample(get_all_ids, k=int(num_random))
        print('first line')
    except Exception as e:
        try:
            random_ids = random.sample(get_all_ids, k=10)
            print('second line')
        except Exception as e:
            # if the user send a wrong value, API return 10 questions by default
            # # random_ids = random.sample(get_all_ids, k=10)
            return Response({
                'queryset': {
                    "message": "Random sample size is greater than size of questions in database. If you have an admin previlege or permission, please add more question, at least > 10."
                    }
                }, status=status.HTTP_400_BAD_REQUEST)
    

    # this will take the previously queryset and then filter based on the randomly picked id's
    random_query= queryset.filter(pk__in=random_ids)
    print(list(random_query.values_list('id', flat=True)))
    serializer = getQuizQuestionsSerializers(random_query, many=True)
    
    return Response({
        'queryset': serializer.data
    }, status=status.HTTP_200_OK)
