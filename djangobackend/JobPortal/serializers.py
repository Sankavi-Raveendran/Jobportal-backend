from rest_framework import serializers
from JobPortal.models import jobs

class JobsSerializer(serializers.ModelSerializer):
    class Meta:
        model = jobs
        fields = '__all__'