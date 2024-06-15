from django.db import models


class TimeReport(models.Model):
    workspace_id = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    time_taken = models.CharField(max_length=100)
    url = models.URLField(max_length=200)

    def __str__(self):
        return self.workspace_id
