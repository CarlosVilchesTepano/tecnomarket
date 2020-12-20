from django.db.models import fields
from django.db.models.base import Model
from django.db.models.query import QuerySet
from .models import Marca, Producto
from rest_framework import serializers

#Serializador para API Rest Framework
#Funciones de la API
#filtrar los productos y Marcas por indicio y por nombre
#http://localhost:8000/api/producto/?nombre=p
#Ingresar a la API
#http://localhost:8000/api/

class MarcaSerializer(serializers.ModelSerializer):
    class Meta:
        model= Marca
        fields= "__all__"


class ProductoSerializer(serializers.ModelSerializer):
    nombre_marca = serializers.CharField(read_only= True, source='marca.nombre' )
    marca = MarcaSerializer(read_only=True)
    marca_id = serializers.PrimaryKeyRelatedField(queryset= Marca.objects.all(), source = "marca")
    nombre = serializers.CharField(required = True,min_length=3 )
    
    def validate_nombre(self, value):
        existe = Producto.objects.filter(nombre__iexact= value).exists()
        
        if existe:
            raise serializers.ValidationError("Este producto ya existe")
        return value
        
    
    class Meta:
        model= Producto
        fields = "__all__"
        
        #exclude = ["nombre"] #Ejemplo para excluir un campo

       
