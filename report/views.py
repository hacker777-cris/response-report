from rest_framework.views import APIView
from rest_framework.response import Response


class HealthCheckUp(APIView):
    def get(self, request):
        return Response(
            {
                "success": True,
                "message": "if you can see this the server is running on v1.0.2",
            }
        )
