from rest_framework import status, viewsets

from apps.job.models import Job, Candidate
from apps.job.serializers import CandidateSerializer,  JobSerializer
from rest_framework.response import Response
from apps.users.models import Company
from django.shortcuts import get_object_or_404
from rest_framework.decorators import action
# from apps.job.services import add_candidates_to_job
from apps import job


class JobViewSet(viewsets.ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializer

    def perform_create(self, serializer):
        serializer.save(company=self.request.user.company)

    @action(
        methods=['get', 'post'],
        url_name='candidates',
        detail=False,
        url_path='(?P<job_id>[^/.]+)/candidates',
    )
    def add_candidates(self, request, job_id):
        job = get_object_or_404(Job, pk=job_id)

        if request.method == 'GET':
            serializer = CandidateSerializer(job.candidates.all(), many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

        if request.method == 'POST':
            candidate_id = request.data['candidate_id']
            candidate = Candidate.objects.get(id=candidate_id)
            job.candidates.add(candidate)
            candidate_serializer = CandidateSerializer(job.candidates.all(),many=True)
            return Response(candidate_serializer.data, status=status.HTTP_201_CREATED)


class CandidateViewSet(viewsets.ModelViewSet):
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer

    def perform_create(self, serializer):
        candidate = serializer.save(company=self.request.user.company)
