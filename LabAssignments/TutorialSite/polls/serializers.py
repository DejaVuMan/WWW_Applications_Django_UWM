from rest_framework import serializers
from django.utils import timezone
from .models import Question, Choice, Osoba, Druzyna


class QuestionModelSerializer(serializers.Serializer):
    model = Question
    fields = ['id', 'question_text', 'pub_date']
    read_only_fields = ['id', 'pub_date']


class DruzynaModelSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    nazwa = serializers.CharField(max_length=64)
    kraj = serializers.CharField(max_length=2)

    def create(self, validated_data):
        return Druzyna.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.nazwa = validated_data.get('nazwa', instance.nazwa)
        instance.kraj = validated_data.get('kraj', instance.kraj)
        instance.save()
        return instance


class OsobaModelSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    imie = serializers.CharField(max_length=64)
    nazwisko = serializers.CharField(max_length=64)
    miesiac_urodzenia = serializers.ChoiceField(choices=Osoba.Dates.choices, default=Osoba.Dates.JANUARY)
    druzyna = serializers.PrimaryKeyRelatedField(queryset=Druzyna.objects.all(), allow_null=True)
    data_dodania = serializers.DateTimeField()

    def create(self, validated_data):
        return Osoba.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.imie = validated_data.get('imie', instance.imie)
        instance.nazwisko = validated_data.get('nazwisko', instance.nazwisko)
        instance.miesiac_urodzenia = validated_data.get('miesiac_urodzenia', instance.miesiac_urodzenia)
        instance.druzyna = validated_data.get('druzyna', instance.druzyna)
        instance.save()
        return instance

    def validate_imie(self, value):
        if not value.isalpha():
            raise serializers.ValidationError("Name must be only letters")
        return value

    def validate_nazwisko(self, value):
        if not value.isalpha():
            raise serializers.ValidationError("Name must be only letters")
        return value

    def validate_data_dodania(self, value):
        if value > timezone.now():
            raise serializers.ValidationError("Date added cannot be in the future")
        return value


class ChoiceModelSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    question = serializers.PrimaryKeyRelatedField(queryset=Question.objects.all(), allow_null=True)
    choice_text = serializers.CharField(required=True)
    votes = serializers.IntegerField()

    def create(self, validated_data):
        return Choice.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.question = validated_data.get('question', instance.question)
        instance.choice_text = validated_data.get('choice_text', instance.choice_text)
        instance.votes = validated_data.get('votes', instance.votes)
        instance.save()
        return instance
