from rest_framework import serializers

from apps.job.models import Candidate, Job


class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        exclude = ['company']


class CandidateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidate
        exclude = ['company', 'jobs']


class JobCandidateSerializer(serializers.Serializer):
    candidates = serializers.PrimaryKeyRelatedField(queryset=Candidate.objects.values_list('id', flat=True))
