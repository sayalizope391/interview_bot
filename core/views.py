from django.shortcuts import render

# Create your views here.
# core/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import JobPost
from .serializers import JobPostSerializer
from .models import Job, Candidate
from .serializers import DashboardSerializer
from .serializers import SubvendorJobPostSerializer
class JobPostCreateView(APIView):
    def post(self, request):
        serializer = JobPostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Job posted successfully', 'data': serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class VendorDashboardAPIView(APIView):
     def get(self, request):
        active_jobs = Job.objects.filter(is_active=True).count()
        total_jobs = Job.objects.all().count()
        in_pipeline = Candidate.objects.filter(status="in pipeline").count()
        processed = Candidate.objects.filter(is_processed=True).count()

        data = {
            "active_job_listings": active_jobs,
            "total_job_openings": total_jobs,
            "candidates_in_pipeline": in_pipeline,
            "applications_processed": processed
        }
        serializer = DashboardSerializer(data)
        return Response(serializer.data)
class SubvendorJobListView(APIView):
    def get(self, request):
        jobs = JobPost.objects.all()
        serializer = SubvendorJobPostSerializer(jobs, many=True)
        return Response(serializer.data)
