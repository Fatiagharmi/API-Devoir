from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import UserList,OrderDetail,OrderList
from . views import UserDetail
urlpatterns = [
    path('users/', UserList.as_view()),
    path('users/<int:pk>/', UserDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)

urlpatterns = [
    # code omitted for brevity
    path('orders/', OrderList.as_view()),
    path('orders/<int:pk>/', OrderDetail.as_view()),
]