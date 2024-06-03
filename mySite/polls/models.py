from django.db import models


# MODELS
# Defining question text and pub date in Question model
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    # Return question text
    def __str__(self):
        return self.question_text


# Defining question, choice and votes in Choice model
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    # Return choice text
    def __str__(self):
        return self.choice_text
