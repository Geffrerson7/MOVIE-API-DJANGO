from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view=get_schema_view(
    openapi.Info(
        title="Movie API",
        default_version="v1",
        description="API Django",
        terms_of_service="https://policies.google.com/terms",
        contact=openapi.Contact(email="gefferson.casasola@gmail.com"),
        license=openapi.License(name="MIT License"),
    )
)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('movie/', include("movie.urls")),
    path('user/', include("user.urls")),
    path('rent/', include("rent.urls")),
    path('swagger/', schema_view.with_ui("swagger", cache_timeout=0), name='schema-swagger-ui')
]
