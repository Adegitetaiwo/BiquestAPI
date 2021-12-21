from django.urls import path, include
from . import views
urlpatterns = [
    # path('quiz/?rand=10', views.quiz_questions)
    path('quiz/', views.quiz_questions),
]
