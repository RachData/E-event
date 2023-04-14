from rest_framework import status, generics
from rest_framework.response import Response
from social_django.utils import load_strategy, load_backend
from social_core.exceptions import MissingBackend, AuthAlreadyAssociated
from conduit.apps.authentication.serializers import UserSerializer

class GoogleAuthView(generics.GenericAPIView):
    def get(self, request, *args, **kwargs):
        strategy = load_strategy(request)
        backend_name = "google-oauth2"
        
        try:
            backend = load_backend(strategy, backend_name, redirect_uri=None)
        except MissingBackend:
            return Response({"error": "Backend not found"}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            user = backend.do_auth(request.GET.get("code"))
        except AuthAlreadyAssociated:
            return Response({"error": "This Google account is already associated with another user."}, status=status.HTTP_400_BAD_REQUEST)
        
        if user and user.is_active:
            serialized_user = UserSerializer(user)
            return Response(serialized_user.data, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Authentication failed"}, status=status.HTTP_400_BAD_REQUEST)


def google_auth(request):
    strategy = load_strategy(request)
    backend_name = "google-oauth2"
    
    try:
        backend = load_backend(strategy, backend_name, redirect_uri=None)
    except MissingBackend:
        return Response({"error": "Backend not found"}, status=status.HTTP_400_BAD_REQUEST)
    
    try:
        user = request.backend.do_auth(request.GET.get("code"))
    except AuthAlreadyAssociated:
        return Response({"error": "This Google account is already associated with another user."}, status=status.HTTP_400_BAD_REQUEST)
    
    if user and user.is_active:
        serialized_user = UserSerializer(user)
        return Response(serialized_user.data, status=status.HTTP_200_OK)
    else:
        return Response({"error": "Authentication failed"}, status=status.HTTP_400_BAD_REQUEST)