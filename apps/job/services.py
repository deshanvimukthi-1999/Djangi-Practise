
from apps.users.models import Company, User
from apps.job.models import Candidate
from django.shortcuts import get_object_or_404
from django.core.exceptions import ValidationError
from apps.job.serializers import CandidateSerializer


def add_candidates_to_job(request_data, job, company, user):
    data_arr = []

    for candidate in request_data['candidates']:
        data = [{'candidate': candidate, 'job': job.id}]
        candidate = Candidate.objects.get(pk=candidate)
        if candidate.company == user.company:
            data_arr.append(data)
            serializer = CandidateSerializer(data=data, many=True)
            if serializer.is_valid(raise_exception=True):
                candidate = serializer.save()
