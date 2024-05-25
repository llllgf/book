from .views import *
from django.urls import path

urlpatterns = [
    # path('login/',userLogin.as_view(),name='login'),
    # path('logout/',userLogout.as_view(),name='logout')
    path('add_book/', add_book, name='add_book'),
    path('feedback/', feedback, name='feedback'),
    path('home/', home, name='manager_index'),
    path('reply/', reply, name='reply'),
    path('grade_list/', grade_list),
    path('grade_about/<int:id>', grade_about),
    path('students_all/<int:page>', students_all),
    path('add_student/', add_student),
    path('edit_student/<int:id>', edit_student),
]
