from django.urls import path,include

from .views import ClientListViewSet, AdminListViewSet,TokenView

from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt import views as jwt_views


router = DefaultRouter()
router.register(r'clients', ClientListViewSet)
router.register(r'admins', AdminListViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('token/', TokenView.as_view(), name='token_obtain_pair'),
    path('api/refresh/', jwt_views.TokenRefreshView.as_view(), name='refresh'),
]