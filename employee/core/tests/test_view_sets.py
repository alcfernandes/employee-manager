from rest_framework.test import APIRequestFactory
from rest_framework.test import APITestCase

from ..api.viewsets import EmployeeViewSet
from ..models import Employee, Department


class APIEmployeesViewSetsTest(APITestCase):

    def test_view_set(self):
        request = APIRequestFactory().get("")

        employee_detail = EmployeeViewSet.as_view({'get': 'retrieve'})

        arnaldo = Employee.objects.create(
            name="Arnaldo Pereira",
            email="arnaldo@teste.com",
            department=Department.objects.create(name="Architecture")
        )

        response = employee_detail(request, pk=arnaldo.pk)

        self.assertEqual(response.status_code, 200)
