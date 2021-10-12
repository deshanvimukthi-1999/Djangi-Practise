from rest_framework import status, viewsets

from apps.job.models import Job, Candidate
from apps.job.serializers import CandidateSerializer, JobSerializer
from requests.models import Response


class JobViewSet(viewsets.ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializer

    def perform_create(self, serializer):
        serializer.save(company=self.request.user.company)


class CandidateViewSet(viewsets.ModelViewSet):
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer

    # def create_candidate(self, data):
    #     candidate = Candidate(
    #         name=data['name'],
    #         nic=data['nic'],
    #         contact_number=data['contact_number']
    #     )
    #     candidate.save()
    #     return candidate

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
