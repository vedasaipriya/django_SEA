from django.urls import path
from .views import home, login,insert_emp,register,view_all

urlpatterns = [
    path('', register),
    path('login/', login),
    path('home/', home),
    path('insert/',insert_emp),
    path('viewall/',view_all)
]
