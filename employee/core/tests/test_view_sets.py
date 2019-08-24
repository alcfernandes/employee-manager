from django.contrib.auth.models import User
from rest_framework.test import APIRequestFactory
from rest_framework.test import APITestCase
from rest_framework.test import force_authenticate

from ..api.viewsets import EmployeeViewSet
from ..models import Employee, Department
from ..util.api_test_helpers import get_token


class APIEmployeesViewSetsTest(APITestCase):
    fixtures = ['user.json']

    def test_view_set(self):
        request = APIRequestFactory().get("")

        user = User.objects.get(id=1)
        force_authenticate(request, user=user, token=get_token(self.client))

        employee_detail = EmployeeViewSet.as_view({'get': 'retrieve'})

        arnaldo = Employee.objects.create(
            name="Arnaldo Pereira",
            email="arnaldo@teste.com",
            department=Department.objects.create(name="Architecture")
        )

        response = employee_detail(request, pk=arnaldo.pk)

        self.assertEqual(response.status_code, 200)
