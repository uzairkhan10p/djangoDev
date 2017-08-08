from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=500)
    pub_date = models.DateTimeField('Date Published')


class Choice(models.Model):
    question = models.ForeignKey(Question, models.CASCADE)
    choice_text = models.CharField(max_length=100)
    votes = models.IntegerField(default=0)