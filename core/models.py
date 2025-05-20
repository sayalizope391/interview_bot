from django.db import models

# Create your models here.
# core/models.py


class JobPost(models.Model):
    INDUSTRY_CHOICES = [
        ('IT', 'Information Technology'),
        ('FIN', 'Finance'),
        ('EDU', 'Education'),
        ('MKT', 'Marketing'),
        ('OTH', 'Other'),
    ]

    JOB_TYPE_CHOICES = [
        ('FT', 'Full-time'),
        ('PT', 'Part-time'),
        ('IN', 'Internship'),
        ('CT', 'Contract'),
    ]

    organization_name = models.CharField(max_length=255)
    job_industry = models.CharField(max_length=50, choices=INDUSTRY_CHOICES)
    job_type = models.CharField(max_length=50, choices=JOB_TYPE_CHOICES)
    job_title = models.CharField(max_length=255)
    skills = models.TextField(blank=True, null=True)
    job_location = models.CharField(max_length=255)
    company_overview = models.TextField()
    eligible_courses = models.CharField(max_length=255)
    eligibility_criteria = models.TextField()
    email = models.EmailField()
    ctc = models.CharField(max_length=50)
    posted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.job_title} at {self.organization_name}"
from django.db import models

class Job(models.Model):
    title = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    industry = models.CharField(max_length=100)
    job_type = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    company_overview = models.TextField()
    eligible_courses = models.CharField(max_length=255)
    eligibility_criteria = models.TextField()
    email = models.EmailField()
    ctc = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

class Candidate(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    status = models.CharField(max_length=50)  # e.g., "in pipeline", "processed"
    is_processed = models.BooleanField(default=False)
