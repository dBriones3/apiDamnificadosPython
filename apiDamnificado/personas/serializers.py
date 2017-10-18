from rest_framework import serializers
from .models import Personas

SEXOS = (("M","MUJER"),("H","Hombre"),("I", "Indefinido"))
TIPOSPERSONAS = (("Voluntario","Voluntario"), ("Damnificado","Damnificado"), ("Otro","Otro"))

def validar_edad(source):
    if source <= 100:
        pass
    else:
        raise serializers.ValidationError("No debe tener una edad mayor a 100")
        pass

class PeopleGetName(serializers.Serializer):
    nombre = serializers.CharField(max_length=50)

class PersonasCreationSerializer(serializers.Serializer):
    nombre = serializers.CharField(max_length=50)
    edad = serializers.IntegerField(validators=[validar_edad])
    sexo = serializers.CharField(max_length=2)
    tipo_de_personas = serializers.CharField(max_length=50)

    def create(self, validated_data):
        return Personas.objects.create(**validated_data)

class PersonasModifieSerializer(serializers.Serializer):
    tipo_de_personas = serializers.CharField(max_length=50)

class PersonasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Personas
        fields = ['nombre','edad','sexo','tipo_de_personas','id']