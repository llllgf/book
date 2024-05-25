from .views import *
from django.urls import path



urlpatterns = [
    # path('login/',userLogin.as_view(),name='login'),
    # path('logout/',userLogout.as_view(),name='logout')
    path('add_book/', add_book, name='add_book'),
    path('feedback/', feedback, name='feedback'),
    path('home/', home, name='manager_index'),
    path('reply/', reply, name='reply'),
    path('class_list',class_list)
]