from django.test import TestCase

from model_mommy import mommy

from employee.core.models import Department, Employee


class DepartmentModelTest(TestCase):
    def setUp(self):
        self.department = Department(
            name="Architecture"
        )
        self.department.save()

    def test_new_department_was_saved(self):
        self.assertTrue(Department.objects.exists())

    def test_str_return_department_name(self):
        self.assertEqual('Architecture', str(self.department))


class EmployeeModelTest(TestCase):
    def setUp(self):
        self.architecture = mommy.make(Department, name='Architecture')

        self.new_employee = {
            "name": "Arnaldo Pereira",
            "email": "arnaldo@teste.com",
            "department": self.architecture
        }

        self.employee = Employee(**self.new_employee)
        self.employee.save()

    def test_new_employee_was_saved(self):
        self.assertTrue(Employee.objects.exists())

    def test_str_return_employee_name(self):
        self.assertEqual(self.new_employee["name"], str(self.employee))

