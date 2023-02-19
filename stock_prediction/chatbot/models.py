from django.db import models
from chatbot import QuestionAnswer
# Create your models here.
from django.db import models

class QuestionAnswer(models.Model):
    question = models.CharField(max_length=200)
    answer = models.TextField()

    def __str__(self):
        return self.question