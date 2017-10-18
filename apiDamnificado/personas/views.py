from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .models import Personas
from .serializers import PeopleGetName,PersonasCreationSerializer,PersonasSerializer
import requests
import json

# Create your views here.
class PersonasApi(APIView):

    def get(self, request):
        people = Personas.objects.all()
        serializer = PersonasSerializer(people, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = PersonasSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            self._sendPushNotification("Se creo una persona","c_4abhx1yXo:APA91bGzgeruvxvn12Q8Nx7_rADqs5-p5ezZOa97D6qeGfrex-NjejTl2KgX8KR_0AEphI65KaN_hDxr6N7nPIvUBsfxwfR7yTYYecJnRb6wYC8h56RqR0C5zTtAQ9q-1b5PtbxH2UbU")
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def _sendPushNotification(self, message, token):
        baseUrl = "https://fcm.googleapis.com/fcm/send"
        headers = {"Authorization":"key=AIzaSyB0k006LxEMxjpcL1bgz6CkAtEhX2UjQdY","Content-Type":"application/json"}
        data = {  "notification": {"title": message,"body": "5 to 1","icon": "firebase-logo.png","click_action": "http://localhost:8081"},"to" : token}
        data = json.dumps(data)
        pushNotification = requests.post(baseUrl,headers=headers, data=data)
        pushNotificationJson =pushNotification.json()
        if pushNotification.status_code == 200 and "error" not in pushNotificationJson['results'][0]:
            return True
        else:
            return False

class PersonaApi(APIView):
    def _getPersona(self, pk):
        try:
            return Personas.objects.get(pk=pk)
        except Personas.DoesNotExist:
            raise status.HTTP_404_NOT_FOUND

    def get(self, request, pk):
        persona = self._getPersona(pk)
        selializer = PersonasSerializer(persona)
        return Response(selializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        persona = self._getPersona(pk)
        serializer = PersonasSerializer(persona, request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk):
        persona = self._getPersona(pk)
        persona.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
