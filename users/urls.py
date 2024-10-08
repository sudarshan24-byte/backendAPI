from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import UserAPI, home


urlpatterns = [
    path('', home, name='home'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/user', UserAPI.as_view()),
    # path('api/logout', logout, name='refresh_token'),
    # path('api/logout-all', logout_all)
]