from rest_framework import status, viewsets

from apps.job.models import Job, Candidate
from apps.job.serializers import CandidateSerializer, JobSerializer
from requests.models import Response
from apps.users.models import Company
from django.shortcuts import get_object_or_404
from rest_framework.decorators import action
from apps.job.services import add_candidates_to_job


class JobViewSet(viewsets.ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializer

    def perform_create(self, serializer):
        serializer.save(company=self.request.user.company)

    @action(
        methods=['get', 'post'],
        detail=False,
        url_path='(?P<job_id>[^/.]+)/candidates',
    )
    def add_candidates(self, request, job_id):
        jobs= get_object_or_404(self.request.user.company.jobs, pk=job_id)
        company = self.request.user.company

        if request.method == 'GET':
            serializer = CandidateSerializer(job.candidates, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

        if request.method == 'POST':
            # serializer = CandidateSerializer(job.candidates, many=True)
            # if serializer.is_valid(raise_exception=True):
            #     candidate = serializer.save(company=self.request.user.company)
            #     job.company.add(candidate)
            data = add_candidates_to_job(request.data, job, request.user,company)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


class CandidateViewSet(viewsets.ModelViewSet):
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer

    def perform_create(self, serializer):
        candidate = serializer.save(company=self.request.user.company)
