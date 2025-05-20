# core/serializers.py
from rest_framework import serializers
from .models import JobPost
import re

class JobPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobPost
        fields = '__all__'


class DashboardSerializer(serializers.Serializer):
    active_job_listings = serializers.IntegerField()
    total_job_openings = serializers.IntegerField()
    candidates_in_pipeline = serializers.IntegerField()
    applications_processed = serializers.IntegerField()
class SubvendorJobPostSerializer(serializers.ModelSerializer):
    company_overview = serializers.SerializerMethodField()
    class Meta:
        model = JobPost
        fields = [
            "job_industry",
            "job_type",
            "job_title",
            "job_location",
            "company_overview",
            "eligible_courses",
            "eligibility_criteria",
            "ctc"
        ]
    def get_company_overview(self, obj):
        """
        Replace the actual company name (organization_name) with 'this company'
        in the company_overview field.
        """
        if obj.organization_name and obj.company_overview:
            pattern = re.compile(re.escape(obj.organization_name), re.IGNORECASE)
            return pattern.sub("this company", obj.company_overview)
        return obj.company_overview