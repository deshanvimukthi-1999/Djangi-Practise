from rest_framework import viewsets

from apps.job.models import Job
from apps.job.serializers import JobSerializer


class JobViewSet(viewsets.ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user.company)

