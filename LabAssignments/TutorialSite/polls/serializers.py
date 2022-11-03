from rest_framework import serializers
from .models import Question, Choice

class QuestionSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    question_text = serializers.CharField(required=True, allow_blank=False, max_length=200)
    pub_date = serializers.DateTimeField()

    def create(self, validated_data):
        """
        Create and return a new `Question` instance, given the validated data.
        """
        return Question.objects.create(**validated_data)
