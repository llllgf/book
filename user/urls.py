from .views import *
from django.urls import path

urlpatterns = [
    # path('home/', home, name="index"),
    path('book_table/', bookTable, name="book_table"),
    path('home/', home, name="user_index"),

]
