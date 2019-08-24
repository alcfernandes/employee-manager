from rest_framework import status
from rest_framework.test import APITestCase

from ..models import Department, Employee
from ..util.api_test_helpers import get_token


def create_test_data(self):
    architecture = Department.objects.create(name="Architecture")
    ecommerce = Department.objects.create(name="E-commerce")
    mobile = Department.objects.create(name="Mobile")

    self.arnaldo = Employee.objects.create(
        name="Arnaldo Pereira",
        email="arnaldo@teste.com",
        department=architecture
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
