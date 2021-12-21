from typing import ClassVar
from django.db import models


class QuizArchive(models.Model):

    Choice = (
    ('option_one', 'Option One'),
    ('option_two', 'Option Two'),
    ('option_three', 'Option Three'),
    ('option_four', 'Option Four'),
    )
    
    question = models.TextField()
    option_one = models.CharField(max_length=350)
    option_two = models.CharField(max_length=350, blank=True)
    option_three = models.CharField(max_length=350, blank=True)
    option_four = models.CharField(max_length=350, blank=True)
    correct_anwser = models.CharField(max_length=150, choices=Choice)

    def __str__(self):
        return self.question
    
    class Meta:
        verbose_name_plural = 'Quiz Archive'
