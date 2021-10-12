from rest_framework import serializers

from apps.job.models import Candidate, Job


class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        exclude = ['company']

class CandidateSerializer(serializers.ModelSerializer):
    class Meta:
        model =  Candidate
        fields = '__all__'