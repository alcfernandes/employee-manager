from django.contrib import admin
from django.urls import path
from rest_framework.routers import DefaultRouter

from employee.core.api.viewsets import ApiVersion, EmployeeViewSet, DepartmentViewSet

app_name = 'core'

router = DefaultRouter()
router.register('version', ApiVersion, base_name='version')
router.register('employees', EmployeeViewSet, base_name='employees')
router.register('departments', DepartmentViewSet, base_name='departments')

urlpatterns = [
    path('admin/', admin.site.urls),
]
