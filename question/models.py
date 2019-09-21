from django.db import models

class Question(models.Model):
    question = models.CharField(max_length=100)

    def __str__(self):
        return self.question

class Choise(models.Model):
    question = models.ForeignKey(Question,on_delete=models.CASCADE)
    c1 = models.CharField(max_length=100)
    v1 = models.IntegerField(default=0)
    c2 = models.CharField(max_length=100)
    v2 = models.IntegerField(default=0)
    c3 = models.CharField(max_length=100)
    v3 = models.IntegerField(default=0)
    c4 = models.CharField(max_length=100)
    v4 = models.IntegerField(default=0)

    def __str__(self):
        return "<Question: %s>" % self.question
