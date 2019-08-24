from rest_framework.test import APITestCase

from ..api.serializers import EmployeeListSerializer, DepartmentSerializer
from ..models import Employee, Department


class APIEmployeesSerializersTest(APITestCase):

    def test_employee_serializer(self):
        arnaldo = Employee.objects.create(
            name="Arnaldo Pereira",
            email="arnaldo@teste.com",
            department=Department.objects.create(name="Architecture")
        )

        employee_serializer = EmployeeListSerializer(arnaldo)

        self.assertIsNotNone(employee_serializer.data)
        self.assertEqual("Arnaldo Pereira", employee_serializer.data['name'])
        self.assertEqual("arnaldo@teste.com", employee_serializer.data['email'])
        self.assertEqual("Architecture", employee_serializer.data['department'])

    def test_department_serializer(self):
        architecture = Department.objects.create(name="Architecture")
        department_serializer = DepartmentSerializer(architecture)

        self.assertIsNotNone(department_serializer.data)
        self.assertEqual(architecture.name, department_serializer.data['name'])
        self.assertEqual(architecture.id, department_serializer.data['id'])
