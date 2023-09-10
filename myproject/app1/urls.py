from django.urls import path
from .views import register,login,home,insert_emp,view_all,update_emp,delete_emp

urlpatterns = [
    path('', register),
    path('login/', login),
    path('home/', home),
    path('insert/',insert_emp),
    path('viewall/',view_all,name="show-emp"),
    path('update/<int:pk>',update_emp),
    path('delete/<int:pk>',delete_emp),

]
