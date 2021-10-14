from rest_framework import status, viewsets

from apps.job.models import Job, Candidate
from apps.job.serializers import CandidateSerializer, JobSerializer
from requests.models import Response
from apps.users.models import Company
from django.shortcuts import get_object_or_404
from apps.job.services import add_candidate_to_job
from rest_framework.decorators import action


class JobViewSet(viewsets.ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializer

    def perform_create(self, serializer):
        serializer.save(company=self.request.user.company)


class CandidateViewSet(viewsets.ModelViewSet):
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer

    @action(
        methods=['get', 'post'],
        detail=False,
        # url_path='(?P<pk>[^/.]+)/candidates',
    )
    def candidates(self, request, job_id):
        job = get_object_or_404(self.request.user.company.jobs, pk=job_id)
        company = self.request.user.company

        if request.method == 'GET':
            serializer = CandidateSerializer(job.candidates, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

        if request.method == 'POST':
            data = add_candidate_to_job(
                request.data, job, request.user, company)
            return Response(data, status=status.HTTP_201_CREATED)

        return Response({}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def get(self, request, format=None):
        candidate = Candidate.objects.all().order_by('id')
        serializer = CandidateSerializer(candidate, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CandidateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format=None):
        candidate = self.get_object(pk)
        serializer = CandidateSerializer(candidate, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        candidate = self.get_object(pk)
        candidate.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
