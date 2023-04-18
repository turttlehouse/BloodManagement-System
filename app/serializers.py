from rest_framework import  serializers
from .models import blood

class bloodserializer(serializers.ModelSerializer):
    class Meta:
        model= blood
        fields='__all__'