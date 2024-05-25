from .views import *
from django.urls import path

urlpatterns = [
    # path('login/',userLogin.as_view(),name='login'),
    # path('logout/',userLogout.as_view(),name='logout')
    path('add_book/', add_book, name='add_book'),
    path('feedback/', feedback, name='feedback'),
    path('home/', home, name='manager_index'),
    path('reply/', reply, name='reply'),
    path('grade_all/<int:page>', grade_all),
    path('grade_about/<int:id>', grade_about),
    path('students_all/<int:page>', students_all),
    path('add_student/', add_student),
    path('edit_student/<int:id>', edit_student),
    path('add_grade/', add_grade),
    path('book_all/<int:page>', book_all),
    path('add_book/', add_book),
]
