from import_export import resources
from .models import Student, Books


class StudentResource(resources.ModelResource):
    class Meta:
        model = Student

class BookResource(resources.ModelResource):
    class Meta:
        model = Books