# candidate/models.py
from django.db import models


class Candidate(models.Model):
    # Basic information
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()

    # Additional fields
    bio = models.TextField(blank=True, null=True)
    contact_details = models.TextField(blank=True, null=True)
    skills_and_competencies = models.TextField(blank=True, null=True)
    education = models.TextField(blank=True, null=True)
    work_experience = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

