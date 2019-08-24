from django.contrib.auth.models import User
from rest_framework.test import APIRequestFactory
from rest_framework.test import APITestCase
from rest_framework.test import force_authenticate

from ..api.viewsets import EmployeeViewSet, DepartmentViewSet
from ..models import Employee, Department
from ..util.api_test_helpers import get_token


class APIEmployeesViewSetsTest(APITestCase):
    fixtures = ['user.json']

    def setUp(self):
        self.request = APIRequestFactory().get("")
        user = User.objects.get(id=1)
        force_authenticate(self.request, user=user, token=get_token(self.client))

    def test_employee_view_set(self):
        employee_detail = EmployeeViewSet.as_view({'get': 'retrieve'})

        arnaldo = Employee.objects.create(
            name="Arnaldo Pereira",
            email="arnaldo@teste.com",
            department=Department.objects.create(name="Architecture")
        )

        response = employee_detail(self.request, pk=arnaldo.pk)

        self.assertEqual(response.status_code, 200)

    def test_department_view_set(self):
        department_detail = DepartmentViewSet.as_view({'get': 'retrieve'})

        mobile = Department.objects.create(name="Mobile")

        response = department_detail(self.request, pk=mobile.pk)

        self.assertEqual(response.status_code, 200)
