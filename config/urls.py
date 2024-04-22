from django.contrib import admin
from django.urls import path, re_path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from rest_framework.routers import DefaultRouter
from tours.views import CategoryViewSet, TourViewSet, ReviewViewSet
from bookings.views import BookingViewSet



schema_view = get_schema_view(
    openapi.Info(
        title="NeoTour API",
        default_version='v1',
        description="API for NeoTour application",
        # terms_of_service="URL to the terms of service",
        # contact=openapi.Contact(email="Your contact email"),
        # license=openapi.License(name="Your license"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'tours', TourViewSet)
router.register(r'reviews', ReviewViewSet)
router.register(r'bookings', BookingViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),

    # Swagger documentation
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
