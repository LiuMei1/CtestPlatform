
from django.urls import path
from  ctest.views import *

urlpatterns = [

    path('case/',case_index),
    path('case_add/',case_add),

    path('interface/',interface_index),
    path('interface_add/',interface_add),
    path('interface_del/',interface_del),
    path('interface_exe/',interface_exe),
]