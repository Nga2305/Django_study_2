from django.db import models

# Create your models here.
## PART 2
## In our poll app, we’ll create two models: Question and Choice. 
## A Question has a question and a publication date. A Choice has two fields: the text of the choice and a vote tally. 
## Each Choice is associated with a Question.

class Question(models.Model):
    def __str__(self):
        return self.question_text
        # question_text = models.CharField(max_length=200)
        # pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    def __str__(self):
        return self.choice_text
    # question = models.ForeignKey(Question, on_delete=models.CASCADE)
    # choice_text = models.CharField(max_length=200)
    # votes = models.IntegerField(default=0)


# Field class: CharFeild, DateTimeFeild,... -  This tells Django what type of data each field holds.
# name of each Feild: question_text, pub_date, question, choice_text, votes - . You’ll use this value in your Python code, and your database will use it as the column name.
# the option arguments in Feild: efined a human-readable name (ex: 'date published'), max_length, default value (ex: 0 in "votes")
# using ForeignKey. That tells Django each Choice is related to a single Question. Django supports all the common database relationships: many-to-one, many-to-many, and one-to-one.
