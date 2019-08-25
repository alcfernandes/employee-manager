from django_filters import rest_framework as filters
from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from employee.api_version import API_Version
from .serializers import EmployeeListSerializer, EmployeeSerializer, DepartmentSerializer
from ..models import Employee, Department


class ApiVersion(viewsets.ViewSet):

    def list(self, request):
        return Response({'API_Version': API_Version})


class EmployeeViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Employee.objects.all()

    filter_backends = (filters.DjangoFilterBackend, SearchFilter, OrderingFilter)
    filter_fields = ('department', 'email')
    ordering_fields = ('name',)
    search_fields = ('name',)

    def get_serializer_class(self):
        email_filter = self.request.query_params.get('email', None)
        if self.action == 'list' and not email_filter:
            return EmployeeListSerializer

        return EmployeeSerializer


class DepartmentViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

    filter_backends = (filters.DjangoFilterBackend, SearchFilter, OrderingFilter)
    filter_fields = ('name', 'id')
    ordering_fields = ('name',)
    search_fields = ('name',)
