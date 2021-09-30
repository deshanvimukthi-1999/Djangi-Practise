from rest_framework.viewsets import ModelViewSet

from apps.job.models import Job
from apps.job.serializers import JobSerializer


class JobViewSet(ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializer

