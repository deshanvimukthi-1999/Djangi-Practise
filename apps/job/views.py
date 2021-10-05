from rest_framework import status, viewsets
from rest_framework.response import Response

from apps.job.models import Job
from apps.job.serializers import JobSerializer


class JobViewSet(viewsets.ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializer

    def create_job(self, request, pk=None):
        job = self.get_object()
        serializer = JobSerializer(data=request.DATA)
        if serializer.is_valid():
            job.create_job(serializer.data['job'])
            job.save()
            return Response({'status': 'Job is created'})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

