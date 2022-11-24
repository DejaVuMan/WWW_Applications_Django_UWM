from django.shortcuts import render

from rest_framework import status
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from .models import Osoba, Druzyna
from .serializers import OsobaModelSerializer, DruzynaModelSerializer
from django.http import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


@api_view(['GET'])
def person_list(request):
    if request.method == 'GET':
        persons = Osoba.objects.all()
        serializer = OsobaModelSerializer(persons, many=True)
        return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticatedOrReadOnly])
def person_detail(request, pk):
    try:
        person = Osoba.objects.get(pk=pk)
    except Osoba.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        person = Osoba.objects.get(pk=pk)
        serializer = OsobaModelSerializer(person)
        return Response(serializer.data)

@api_view(['PUT', 'DELETE'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def person_update_delete(request, pk):
    try:
        person = Osoba.objects.get(pk=pk)
    except Osoba.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = OsobaModelSerializer(person, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        person.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def team_list(request):

    if request.method == 'GET':
        teams = Druzyna.objects.all()
        serializer = DruzynaModelSerializer(teams, many=True)
        return Response(serializer.data)


@api_view(['GET', 'PUT', 'DELETE'])
def team_detail(request, pk):
    try:
        team = Druzyna.objects.get(pk=pk)
    except Druzyna.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        team = Druzyna.objects.get(pk=pk)
        serializer = DruzynaModelSerializer(team)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = DruzynaModelSerializer(team, data=request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        team.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
