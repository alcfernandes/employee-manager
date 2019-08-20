from rest_framework import viewsets
from rest_framework.response import Response

from employee.api_version import API_Version


class ApiVersion(viewsets.ViewSet):

    def list(self, request):
        return Response({'API_Version': API_Version})
