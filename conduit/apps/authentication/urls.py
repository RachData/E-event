from django.urls import path
from .views_google import GoogleAuthView
#from .views_google import google_auth
from .views import (
    LoginAPIView, RegistrationAPIView, UserRetrieveUpdateAPIView
)

urlpatterns = [
    path('user/', UserRetrieveUpdateAPIView.as_view()),
    path('users/', RegistrationAPIView.as_view()),
    path('users/login/', LoginAPIView.as_view()),
    #path("google-auth/", google_auth, name="google-auth"),
    path("google-auth/", GoogleAuthView.as_view(), name="google-auth"),
]
