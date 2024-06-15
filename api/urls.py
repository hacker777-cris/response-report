from django.urls import path
from . import views


urlpatterns = [
    path("get-reports/", views.ReportView.as_view(), name="get-reports"),
    path("get-report/", views.GetCreateReportView.as_view(), name="get-report"),
]
