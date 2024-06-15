from rest_framework import serializers
from .models import TimeReport


class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimeReport
        fields = ["workspace_id", "time_taken", "url", "created_at"]
        read_only_fields = ["created_at"]
