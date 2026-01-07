from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'task', TaskAPIView)

urlpatterns = [
    # path('', include(router.urls)),
    path('task/', task_list_create_api_view),
    path('task/<int:pk>/', task_detail_api_view),
]