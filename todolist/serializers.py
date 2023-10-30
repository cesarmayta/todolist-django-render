from rest_framework import serializers
from .models import Tarea

class TareaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tarea
        fields = '__all__'
        
    def to_representation(self,instance):
        representation = super().to_representation(instance)
        return representation
        
