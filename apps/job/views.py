from rest_framework import status, viewsets

from apps.job.models import Job, Candidate
from apps.job.serializers import CandidateSerializer, JobCandidateSerializer, JobSerializer
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
        job = get_object_or_404(self.request.user.company.jobs, pk=job_id)
        # company = self.request.user.company

        if request.method == 'GET':
            serializer = CandidateSerializer(job.candidates, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

        if request.method == 'POST':
            serializer = JobCandidateSerializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.validated_data['new_candidate'].jobs.add(job)
            return Response(status=status.HTTP_201_CREATED)

            # data = add_candidates_to_job(request.data, job, request.user,company)
            # return Response(data, status=status.HTTP_201_CREATED)


class CandidateViewSet(viewsets.ModelViewSet):
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer

    def perform_create(self, serializer):
        candidate = serializer.save(company=self.request.user.company)
