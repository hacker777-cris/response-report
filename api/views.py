from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import TimeReport
from .serializers import ReportSerializer
from rest_framework import status
from django.utils import timezone


class ReportView(APIView):
    def get(self, request):
        reports = TimeReport.objects.all()
        serializer = ReportSerializer(reports, many=True)
        data = serializer.data
        return Response({"success": True, "data": data})


class GetCreateReportView(APIView):
    def get(self, request):
        workspace_id = request.query_params.get("workspace_id")
        if workspace_id:
            reports = TimeReport.objects.filter(workspace_id=workspace_id)
            if reports.exists():
                serializer = ReportSerializer(reports, many=True)
                return Response(
                    {"success": True, "data": serializer.data},
                    status=status.HTTP_200_OK,
                )
            else:
                return Response(
                    {
                        "success": False,
                        "error": "No reports found for the given workspace ID.",
                    },
                    status=status.HTTP_404_NOT_FOUND,
                )
        else:
            return Response(
                {
                    "success": False,
                    "error": "workspace_id query parameter is required.",
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

    def post(self, request):
        data = request.data
        data["created_at"] = timezone.now()  # Automatically set the created_at field
        serializer = ReportSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
