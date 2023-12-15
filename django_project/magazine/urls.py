from django.urls import path
from .views import magazine_list, add_magazine, magazine_detail

urlpatterns = [
    path('list/', magazine_list, name='magazine_list'),
    path('add/', add_magazine, name='add_magazine'),
    path('<int:magazine_id>/', magazine_detail, name='magazine_detail'),
]
