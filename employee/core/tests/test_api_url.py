from rest_framework import status
from rest_framework.test import APITestCase


class APIUrlTest(APITestCase):

    def test_employee_url(self):
        response = self.client.get('/api/employees/')
        print(response.status_code)
        assert response.status_code == status.HTTP_200_OK

