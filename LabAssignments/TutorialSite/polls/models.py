import datetime
from django.db import models
from django.utils import timezone


## Creating DB updates:
## python manage.py makemigrations CategoryModelName
## python manage.py sqlmigrate CategoryModelName XXXX
## python manage.py migrate

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text


class Osoba(models.Model):
    class Meta:
        ordering = ["nazwisko"]
        verbose_name_plural = "Osoby"

    class Dates(models.IntegerChoices):
        JANUARY = 1
        FEBRUARY = 2
        MARCH = 3
        APRIL = 4
        MAY = 5
        JUNE = 6
        JULY = 7
        AUGUST = 8
        SEPTEMBER = 9
        OCTOBER = 10
        NOVEMBER = 11
        DECEMBER = 12

    imie = models.CharField(max_length=64, blank=False)
    nazwisko = models.CharField(max_length=64, blank=False)
    miesiac_urodzenia = models.CharField(max_length=2, choices=Dates.choices, default='1')
    data_dodania = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.imie + ' ' + self.nazwisko
