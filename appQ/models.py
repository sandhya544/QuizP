from django.db import models


class Question(models.Model):
    qid = models.CharField(primary_key=True, max_length=10, unique=True, default="Q0000")
    question = models.CharField(max_length=500)
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    answer = models.CharField(max_length=100)
    toughness = models.FloatField(default=0)
    topic = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.question


class Result(models.Model):
    rid = models.AutoField(primary_key=True, unique=True)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    score = models.IntegerField(default=0)
    total = models.IntegerField(default=0)
    dateOfTest = models.DateField(auto_now_add=True)
    percentage = models.FloatField(default=0)
    exp_at_test = models.IntegerField(default=0)
    topic = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.email


class Profile(models.Model):
    pid = models.AutoField(primary_key=True)
    mail = models.EmailField(max_length=100,unique=True)
    name = models.CharField(max_length=100)
    exp_level = models.FloatField(default=0)
    aim = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.mail
