from apps.job.models import Candidate
from django.shortcuts import get_object_or_404
from apps.users.models import User
from apps.job.serializers import CandidateSerializer
from uuid import UUID
from django.core.exceptions import ValidationError


def add_candidate_to_job(request_data, job, user, compnay):
    valid_data = []
    invalid_data = []

    for candidate in request_data['candidates']:
        data = [{'candidate': candidate, 'job': job.id}]
        candidate_obj = Candidate.objects.get(pk=candidate)
        if candidate_obj.company == user.company:
            valid_data.append(data)
            serializer = CandidateSerializer(data=data, many=True)
            if serializer.is_valid(raise_exception=True):
                candidateships = serializer.save()

        else:
            invalid_data.append(data)
