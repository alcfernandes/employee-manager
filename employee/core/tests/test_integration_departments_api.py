"""
Integration Tests to Departments API
"""
from rest_framework import status
from rest_framework.test import APITestCase

from ..models import Department
from ..util.api_test_helpers import get_token


def create_test_data(self):
    self.mobile = Department.objects.create(name="Mobile")
    self.ecommerce = Department.objects.create(name="E-commerce")

    self.token = get_token(self.client)


class APIDepartmentsListTest(APITestCase):
    """
    (GET) /api/departments/
    Should return the existing Departments list
    """

    fixtures = ['user.json']

    def setUp(self):
        create_test_data(self)

        self.response = self.client.get('/api/departments/', HTTP_AUTHORIZATION=f'Bearer {self.token}')

    def test_get(self):
        self.assertEqual(self.response.status_code, status.HTTP_200_OK)

    def test_response(self):
        self.maxDiff = None
        expected = [
            {
                "id": self.mobile.id,
                "name": self.mobile.name
            },
            {
                "id": self.ecommerce.id,
                "name": self.ecommerce.name
            }
        ]

        self.assertJSONEqual(
            str(self.response.content, encoding='utf8'),
            expected
        )


class APIEmployeeRetrieve(APITestCase):
    """
    (GET) /api/departments/<employee_id>
    Should return the Department with the given id
    """

    fixtures = ['user.json']

    def setUp(self):
        create_test_data(self)

    def test_can_retrieve_an_employee(self):
        self.maxDiff = None
        expected = {
            "id": self.mobile.id,
            "name": self.mobile.name
        }
        self.response = self.client.get(f'/api/departments/{self.mobile.id}/',
                                        HTTP_AUTHORIZATION=f'Bearer {self.token}')
        self.assertEqual(self.response.status_code, status.HTTP_200_OK)
        self.assertJSONEqual(
            str(self.response.content, encoding='utf8'),
            expected
        )


class APIDepartmentCreate(APITestCase):
    """
    (POST) /api/departments/
    It should create a new department with the given data
    """

    fixtures = ['user.json']

    def setUp(self):
        self.token = get_token(self.client)

    def test_create(self):
        data_new_department = {
            'name': "Sales"
        }

        self.response = self.client.post('/api/departments/', data_new_department, HTTP_AUTHORIZATION=f'Bearer {self.token}')
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

        self.expected = {
            'id': Department.objects.first().id,
            **data_new_department
        }
        self.assertJSONEqual(
            str(self.response.content, encoding='utf8'),
            self.expected
        )


class APIDepartmentUpdatePatch(APITestCase):
    """
    (PATCH) /api/departments/<employee_id>
    Should update the Department with the given data (even partial data)
    """

    fixtures = ['user.json']

    def setUp(self):
        create_test_data(self)

    def test_can_update(self):
        expected = {
            "id": self.mobile.id,
            "name": "Name Changed"
        }

        payload = {
            'name': 'Name Changed'
        }

        self.response = self.client.patch(f'/api/departments/{self.mobile.id}/', payload, HTTP_AUTHORIZATION=f'Bearer {self.token}')
        self.assertEqual(self.response.status_code, status.HTTP_200_OK)
        self.assertJSONEqual(
            str(self.response.content, encoding='utf8'),
            expected
        )


class APIDepartmentDestroy(APITestCase):
    """
    (DEL) /api/departments/<employee_id>
    Should delete the Department with the given id
    """
    fixtures = ['user.json']

    def setUp(self):
        create_test_data(self)

    def test_can_delete(self):
        self.response = self.client.delete('/api/departments/1/', HTTP_AUTHORIZATION=f'Bearer {self.token}')
        self.assertEqual(self.response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Department.objects.count(), 1)

