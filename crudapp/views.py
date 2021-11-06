from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . models import Note
from . serializers import NoteSerializer
from rest_framework.decorators import api_view, authentication_classes
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token


class NoteList(APIView):
    authentication_classes = [SessionAuthentication,
                              BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        current_user = request.user
        user = User.objects.get(id=current_user.id)
        note = Note.objects.filter(user=user)
        serializer = NoteSerializer(note, many=True)
        return Response(serializer.data)


class NoteDetail(APIView):
    authentication_classes = [SessionAuthentication,
                              BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return Note.objects.get(pk=pk)
        except Note.DoesNotExist:
            return Response("Invalid Response")

    def get(self, request, pk):
        current_user = request.user
        user = User.objects.get(id=current_user.id)
        note = Note.objects.get(id=pk, user=user)
        serializer = NoteSerializer(note, many=False)
        return Response(serializer.data)


class NoteCreate(APIView):
    authentication_classes = [SessionAuthentication,
                              BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        current_user = request.user
        user = User.objects.get(id=current_user.id)
        serializer = NoteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=user)
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class NoteUpdate(APIView):
    authentication_classes = [SessionAuthentication,
                              BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def put(self, request, pk):
        current_user = request.user
        user = User.objects.get(id=current_user.id)
        note = Note.objects.get(id=pk, user=user)
        serializer = NoteSerializer(instance=note, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)


class NoteDelete(APIView):
    authentication_classes = [SessionAuthentication,
                              BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def delete(self, request, pk):
        current_user = request.user
        user = User.objects.get(id=current_user.id)
        note = Note.objects.get(id=pk, user=user)
        note.delete()
        return Response("Note deleted!", status=200)
