from django.db import models

from apps.users.models import User, Company


class Job(models.Model):
    role = models.CharField(max_length=200)
    company = models.ForeignKey(
        Company, related_name='jobs', on_delete=models.CASCADE)


class Section(models.Model):
    name = models.CharField(max_length=200)
    job = models.ForeignKey(Job, related_name='sections',
                            on_delete=models.CASCADE)


class Question(models.Model):
    question_type = models.CharField(max_length=100)
    documents = models.CharField
    section = models.ForeignKey(
        Section, related_name='questions', on_delete=models.CASCADE)


class Assessor(models.Model):
    name = models.CharField(max_length=200)
    documents = models.CharField(max_length=200)
    user = models.ForeignKey(
        User, related_name='assessors', on_delete=models.CASCADE)
    jobs = models.ManyToManyField(Job, related_name='assessors')


class Interview(models.Model):
    assessor = models.ForeignKey(
        Assessor, related_name='interviews', on_delete=models.CASCADE)
    job = models.ForeignKey(
        Job, related_name='interviews', on_delete=models.CASCADE)


class Candidate(models.Model):
    name = models.CharField(max_length=100)
    nic = models.IntegerField()
    contact_number = models.IntegerField()
    jobs = models.ManyToManyField(Job, related_name='candidates')
    company = models.ForeignKey(
        Company, related_name='candidates', on_delete=models.CASCADE)


class Experience(models.Model):
    placed_work = models.CharField(max_length=100)
    time_period = models.DateTimeField
    role = models.CharField(max_length=100)
    candidate = models.ForeignKey(
        Candidate, related_name='experiences', on_delete=models.CASCADE)
