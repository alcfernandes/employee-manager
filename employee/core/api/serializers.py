from rest_framework import serializers

from ..models import Employee, Department


class DepartmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Department
        fields = ('id', 'name')


class EmployeeListSerializer(serializers.ModelSerializer):
    department = serializers.SerializerMethodField()

    class Meta:
        model = Employee
        fields = ('name', 'email', 'department')


    def get_department(self, obj):
        return obj.department.name


class EmployeeSerializer(serializers.ModelSerializer):
    department = serializers.PrimaryKeyRelatedField(queryset=Department.objects.all())

    class Meta:
        model = Employee
        fields = ('id', 'name', 'email', 'department')




