
from apps.users.models import Company
from apps.job.models import Candidate


def add_candidate(data):

    # create company for candidate
    company = Company.objects.create()

    # create candidate logic goes here
    candidate = Candidate(
        first_name=data['first_name'],
        last_name=data['last_name'],
        email=data['email'],
        phone=data['phone'],
        workplace=data['workplace'],
        role=data['role'],
        job=data['job'],
        company=company

    )

    candidate.save()

    # Set company job to candidate
    company.job = candidate

    company.save()

    return candidate
