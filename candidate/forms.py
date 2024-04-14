# candidate/forms.py
from django import forms
from .models import Candidate


class CandidateProfileForm(forms.ModelForm):
    class Meta:
        model = Candidate
        fields = ['first_name', 'last_name', 'email', 'bio', 'contact_details', 'skills_and_competencies',
                  'education', 'work_experience']
