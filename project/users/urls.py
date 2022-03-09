from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views import RegisterUsersView

urlpatterns = [
    path('register/', RegisterUsersView.as_view()),
    path('login/', TokenObtainPairView.as_view(), name='token-obtain-pair-view'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token-refresh-view'),
]
