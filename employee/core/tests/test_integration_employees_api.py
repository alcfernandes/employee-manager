"""
Integration Tests to Employees API
"""
from rest_framework import status
from rest_framework.test import APITestCase

from ..models import Department, Employee
from ..util.api_test_helpers import get_token


def create_test_data(self):
    self.architecture = Department.objects.create(name="Architecture")
    ecommerce = Department.objects.create(name="E-commerce")
    mobile = Department.objects.create(name="Mobile")

    self.arnaldo = Employee.objects.create(
        name="Arnaldo Pereira",
        email="arnaldo@teste.com",
        department=self.architecture
    )

    self.renato = Employee.objects.create(
        name="Renato Pedigoni",
        email="renato@teste.com",
        department=ecommerce
    )

    self.thiago = Employee.objects.create(
        name="Thiago Catoto",
        email="cototo@teste.com",
        department=mobile
    )

    self.token = get_token(self.client)


class APIEmployeeListTest(APITestCase):
    """
    (GET) /api/employees/
    Should return the existing Employees list (without ids)
    """

    fixtures = ['user.json']

    def setUp(self):
        create_test_data(self)

        self.response = self.client.get('/api/employees/', HTTP_AUTHORIZATION=f'Bearer {self.token}')

    def test_get(self):
        self.assertEqual(self.response.status_code, status.HTTP_200_OK)

    def test_response(self):
        self.maxDiff = None
        expected = [
            {
                "name": "Arnaldo Pereira",
                "email": "arnaldo@teste.com",
                "department": "Architecture"
            },
            {
                "name": "Renato Pedigoni",
                "email": "renato@teste.com",
                "department": "E-commerce"
            },
            {
                "name": "Thiago Catoto",
                "email": "cototo@teste.com",
                "department": "Mobile"
            }
        ]

        self.assertJSONEqual(
            str(self.response.content, encoding='utf8'),
            expected
        )


class APIEmployeeRetrieve(APITestCase):
    """
    (GET) /api/employees/<employee_id>
    Should return the Employee with the given id
    """

    fixtures = ['user.json']

    def setUp(self):
        create_test_data(self)

    def test_can_retrieve_an_employee(self):
        self.maxDiff = None
        expected = {
            "id": self.arnaldo.id,
            "name": self.arnaldo.name,
            "email": self.arnaldo.email,
            "department": self.architecture.id
        }
        self.response = self.client.get(f'/api/employees/{self.arnaldo.id}/',
                                        HTTP_AUTHORIZATION=f'Bearer {self.token}')
        self.assertEqual(self.response.status_code, status.HTTP_200_OK)
        self.assertJSONEqual(
            str(self.response.content, encoding='utf8'),
            expected
        )


class APIEmployeesCreate(APITestCase):
    """
    (POST) /api/employee/
    It should create a new employee with the given data
    """

    fixtures = ['user.json']

    def setUp(self):
        self.token = get_token(self.client)
        self.mobile = Department.objects.create(name="Mobile")

    def test_create(self):
        data_new_employee = {
            'name': "Alessandro Fernandes",
            'email': "alcfernandes@yahoo.com",
            'department': 1
        }

        self.response = self.client.post('/api/employees/', data_new_employee, HTTP_AUTHORIZATION=f'Bearer {self.token}')
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

        self.expected = {
            'id': Employee.objects.first().id,
            **data_new_employee
        }
        self.assertJSONEqual(
            str(self.response.content, encoding='utf8'),
            self.expected
        )


class APIEmployeeUpdatePatch(APITestCase):
    """
    (PATCH) /api/employees/<employee_id>
    Should update the Employee with the given data (even partial data)
    """

    fixtures = ['user.json']

    def setUp(self):
        create_test_data(self)

    def test_can_update(self):
        expected = {
            "id": self.arnaldo.id,
            "name": "Name Changed",
            "email": self.arnaldo.email,
            "department": self.architecture.id
        }

        payload = {
            'name': 'Name Changed'
        }

        self.response = self.client.patch(f'/api/employees/{self.arnaldo.id}/', payload, HTTP_AUTHORIZATION=f'Bearer {self.token}')
        self.assertEqual(self.response.status_code, status.HTTP_200_OK)
        self.assertJSONEqual(
            str(self.response.content, encoding='utf8'),
            expected
        )


class APIEmployeeUpdatePut(APITestCase):
    """
    (PUT) /api/employees/<employee_id>
    Should update the Employee with the given data (all data)
    """

    fixtures = ['user.json']

    def setUp(self):
        create_test_data(self)

    def test_can_update(self):
        expected = {
            "id": self.arnaldo.id,
            "name": "Name Changed",
            "email": "new@test.com",
            "department": self.architecture.id
        }

        payload = {
            'name': 'Name Changed',
            'email': 'new@test.com',
            'department': self.architecture.id
        }

        self.response = self.client.put(f'/api/employees/{self.arnaldo.id}/', payload, HTTP_AUTHORIZATION=f'Bearer {self.token}')
        self.assertEqual(self.response.status_code, status.HTTP_200_OK)
        self.assertJSONEqual(
            str(self.response.content, encoding='utf8'),
            expected
        )


class APIEmployeeDestroy(APITestCase):
    """
    (DEL) /api/employees/<employee_id>
    Should delete the Employee with the given id
    """
    fixtures = ['user.json']

    def setUp(self):
        create_test_data(self)

    def test_can_delete(self):
        self.response = self.client.delete('/api/employees/1/', HTTP_AUTHORIZATION=f'Bearer {self.token}')
        self.assertEqual(self.response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Employee.objects.count(), 2)
