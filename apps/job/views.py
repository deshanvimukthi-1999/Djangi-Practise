from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from apps.job.models import Job
from apps.job.serializers import JobSerializer


class JobViewSet(ModelViewSet):

    @api_view(['GET'])
    def jobList(self, request):
        job = Job.objects.all()
        serializer = JobSerializer(job, many=True)
        return  Response(serializer.data)

    @api_view(['POST'])
    def jobCreate(self, request):
        serializer = JobSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

        return Response(serializer.data)

    @api_view(['POST'])
    def jobUpdate(self, request, pk):
        job = Job.objects.get(id=pk)
        serializer = JobSerializer(instance=job, data=request.data)

        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

    @api_view(['DELETE'])
    def jobDelete(self, request, pk):
        job = Job.objects.get(id=pk)
        job.delete()



