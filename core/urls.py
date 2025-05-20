# core/urls.py
from django.urls import path
from .views import JobPostCreateView,VendorDashboardAPIView,SubvendorJobListView


urlpatterns = [
    path('post-job/', JobPostCreateView.as_view(), name='post-job'),
     path('vendor-dashboard/', VendorDashboardAPIView.as_view(), name='vendor-dashboard'),
      path('subvendor/jobs/', SubvendorJobListView.as_view(), name='subvendor-jobs')
]
