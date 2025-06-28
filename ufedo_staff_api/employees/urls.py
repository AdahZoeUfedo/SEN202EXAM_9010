# users/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ManagerViewSet, InternViewSet, StaffBaseViewSet

router = DefaultRouter()
router.register(r'manager', ManagerViewSet)
router.register(r'intern', InternViewSet)
router.register(r'staffbase', StaffBaseViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
