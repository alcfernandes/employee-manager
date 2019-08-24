from rest_framework import serializers

from ..models import Employee, Department


class DepartmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Department
        fields = ('name',)


class EmployeeSerializer(serializers.ModelSerializer):
    department = serializers.SerializerMethodField()

    class Meta:
        model = Employee
        exclude = ('id',)


    def get_department(self, obj):
        return obj.department.name


