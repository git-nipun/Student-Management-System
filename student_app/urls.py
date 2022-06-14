from django.urls import path
from student_app.views import *
urlpatterns = [
    path('home/',home,name='home'),
    path('register/',add,name='register'),
    path('f_register/',add_f,name='f_register'),
    path('search/',show,name='search'),
    path('s_update/<int:id>',update,name='s_update'),
    path('s_delete/<int:id>',delete,name='s_delete')
]
