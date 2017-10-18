from rest_framework import serializers
from .models import Lugares, PersonasHasLugares

class LugaresGetName(serializers.Serializer):
    nombre = serializers.CharField(max_length=50)
    calle = serializers.CharField(max_length=70)
    colonia = serializers.CharField(max_length=50)

class LugaresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lugares
        fields = ['calle','nombre','colonia']

class LugaresHasPersonasGet(serializers.Serializer):
    fecha = serializers.DateField()
    status = serializers.CharField(max_length=20)
    lugares_id = serializers.IntegerField()
    personas_id = serializers.IntegerField()

class LugaresHasPersonasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lugares
        fields = ['fecha','status','lugares_id','personas_id']