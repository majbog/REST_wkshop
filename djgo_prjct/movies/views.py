# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import Http404
from django.shortcuts import render, get_object_or_404

# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import MovieSerializer, PersonSerializer
from .models import Movie, Person


class MoviesView(APIView):
    #
    # def get_object(self):
    #     try:
    #         return Movie.objects.all()
    #     except Movie.DoesNotExist:
    #         raise Http404

    def get(self, request, format=None):
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True, context={"request": request})
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MovieView(APIView):

    def get(self, request, id, format=None):
        movie = get_object_or_404(Movie, id=id)
        serializer = MovieSerializer(movie, context={"request": request})
        return Response(serializer.data)
    def delete(self, request, id, format=None):
        movie = get_object_or_404(Movie, id=id)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    def put(self, request, id, format=None):
        movie = get_object_or_404(id=id)
        serializer = MovieSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




class PeopleView(APIView):

    def get(self, request, format=None):
        movies = Person.objects.all()
        serializer = PersonSerializer(movies, many=True, context={"request": request})
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = PersonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PersonView(APIView):

    def get(self, request, id, format=None):
        person = get_object_or_404(Movie, id=id)
        serializer = PersonSerializer(person, context={"request": request})
        return Response(serializer.data)
    def delete(self, request, id, format=None):
        person = get_object_or_404(Person, id=id)
        person.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    def put(self, request, id, format=None):
        person = get_object_or_404(id=id)
        serializer = PersonSerializer(person, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)






