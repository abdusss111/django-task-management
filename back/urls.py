from django.contrib import admin
from django.urls import path, include

# Define URL patterns
urlpatterns = [
    # Admin panel
    path('admin/', admin.site.urls),

    # Include URLs from the 'core' app
    path('', include('core.urls')),
]
