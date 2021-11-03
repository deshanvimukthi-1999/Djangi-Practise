# from apps.job.models import Candidate
# from apps.job.serializers import CandidateSerializer


# def add_candidate_to_job(request_data, job, user, company):
#     candidate_data = []

#     for candidate in request_data:
#         data = [{'candidate': candidate, 'job': job.id}]
#         candidate_obj = Candidate.objects.get(pk=candidate)
#         if candidate_obj.company == user.company:
#             candidate_data.append(data)
#             serializer = CandidateSerializer(data=data, many=True)
#             if serializer.is_valid(raise_exception=True):
#                 candidateships = serializer.save()
#                 job.add(candidate_data)

#     return {'data': candidate_data}
