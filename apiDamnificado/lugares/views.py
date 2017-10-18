from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .models import Lugares,PersonasHasLugares
from .serializers import LugaresGetName,LugaresSerializer,LugaresHasPersonasGet,LugaresHasPersonasSerializer

# Create your views here.
class LugaresApi(APIView):

    def get(self, request):
        people = Lugares.objects.all()
        serializer = LugaresGetName(people, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = LugaresSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LugaresHasPersonas(APIView):

    def get(self, request):
        luagresPersona = PersonasHasLugares.objects.all()
        serializer = LugaresHasPersonasGet(luagresPersona, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = LugaresSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


