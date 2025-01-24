from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProjectViewSet, TaskViewSet, task_management_view, auth_view
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

# Initialize the DefaultRouter for API endpoints
router = DefaultRouter()
router.register('projects', ProjectViewSet)
router.register('tasks', TaskViewSet)

# Define URL patterns
urlpatterns = [
    # API endpoints for Project and Task ViewSets
    path('api/', include(router.urls)),

    # Custom view for the task management template
    path('template/', task_management_view, name='task_management'),

    # JWT token authentication endpoints
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('auth/', auth_view),
]
