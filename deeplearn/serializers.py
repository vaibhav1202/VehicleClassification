from rest_framework import serializers
from deeplearn.models import deep
class deepSerializer(serializers.ModelSerializer):
    class Meta:
        model = deep
        fields = ("img",)
