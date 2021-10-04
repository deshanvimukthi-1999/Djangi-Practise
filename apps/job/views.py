from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from apps.job.models import Job
from apps.job.serializers import JobSerializer


class JobViewSet(ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializer

    @action(methods=['post', 'get'], detail=True)
    def jobs(self, request):
        job = self.get_object()

        if request.method == 'POST':
            serializer = JobSerializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save(job=job, invited_by=request.user)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            serializer = JobSerializer(job.invitations.all(), many=True)
            return Response(serializer.data)

