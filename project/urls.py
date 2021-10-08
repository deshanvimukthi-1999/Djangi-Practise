from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework.routers import DefaultRouter
from apps.users.views import UserViewSet, RegisterAPIView
from apps.job.views import JobViewSet


router = DefaultRouter()
router.register('users', UserViewSet, basename='users')
router.register('job', JobViewSet, basename='jobs')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    # path('api/auth/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/register/', RegisterAPIView.as_view(), name='register'),
    path('auth/login', TokenObtainPairView, name='login'),
    path('api/auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

#
# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
