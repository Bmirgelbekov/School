from rest_framework import viewsets, permissions
from rest_framework import filters
from .serializers import SchoolSerializer, ClassesSerializer, StudentSerializer
from .models import School, Classes, Student
from django_filters.rest_framework import DjangoFilterBackend




class SchoolViewSet(viewsets.ModelViewSet):
    """ 
    ViewSet для Школы
    """
    queryset = School.objects.all()
    serializer_class = SchoolSerializer
    """ Пермишн чтобы удалять школы мог только Админ """
    def get_permissions(self):
        method = self.request.method
        if method in permissions.SAFE_METHODS:
            self.permission_classes = [permissions.AllowAny]
        elif method in ['POST', 'DELETE']:
            self.permission_classes = [permissions.IsAdminUser]
        return super().get_permissions()


class ClassesViewSet(viewsets.ModelViewSet):
    """ 
    ViewSet для Классов школы
    """
    queryset = Classes.objects.all()
    serializer_class = ClassesSerializer
    """ Пермишн чтобы изменять классы мог только авторизованный пользователь """
    def get_permissions(self):
        method = self.request.method
        if method in permissions.SAFE_METHODS:
            self.permission_classes = [permissions.AllowAny]
        elif method in ['POST', 'DELETE', 'PUT', 'PATCH']:
            self.permission_classes = [permissions.IsAuthenticated]
        return super().get_permissions()


class StudentViewSet(viewsets.ModelViewSet):
    """ 
    ViewSet для получения\изменения Студентов
    """
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    """ позволяет фильтровать студентов по данным тегам """
    filterset_fields = ['gender', 'classes'] 
    """ позволяет произовдить поиска студентов по имени """
    search_fields = ['name']


