from django.test import TestCase
from django.contrib import admin

from employee.core.models import Department, Employee
from employee.core.admin import DepartmentModelAdmin, EmployeeModelAdmin


class DepartmentAdminTest(TestCase):

    def setUp(self):
        self.model_admin = DepartmentModelAdmin(Department, admin.site)

    def test_department_admin_is_registered(self):
        # pylint: disable=W0212
        self.assertTrue(admin.site._registry[Department])

    def test_list_display_fields(self):
        fields_expecteds = [
            'name',
            'id',
        ]

        for field in fields_expecteds:
            with self.subTest():
                self.assertIn(field, self.model_admin.list_display)


class EmployeeAdminTest(TestCase):

    def setUp(self):
        self.model_admin = EmployeeModelAdmin(Employee, admin.site)

    def test_employee_admin_is_registered(self):
        # pylint: disable=W0212
        self.assertTrue(admin.site._registry[Employee])

    def test_list_display_fields(self):
        fields_expecteds = [
            'name',
            'email',
            'department',
            'id',
        ]

        for field in fields_expecteds:
            with self.subTest():
                self.assertIn(field, self.model_admin.list_display)
