# Create your views here.
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
# モデルインポート
from .models import SystemAdminInformation
# シリアライズインポート
from .serializers import MainListSerializer

from .utils.system_admin.auth import SystemAdminAuthentication, SystemAdminJWTAuthentication, SystemAdminCreateAccount, SystemAdminDeleteAccount
from rest_framework import status
from rest_framework.permissions import IsAuthenticated


class SystemAdminAuthenticationView(APIView):
    """
    システム管理者用ログインView
    """
    authentication_classes = [SystemAdminAuthentication]

    def post(self, request, *args, **kwargs):
        return Response({"token": request.user}, status=status.HTTP_200_OK)


class SystemAdminJWTAuthenticationView(APIView):
    """
    システム管理者用JWT認証View
    """
    authentication_classes = [SystemAdminJWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        return Response({"request": "data"}, status=status.HTTP_200_OK)


class SystemAdminCreateAccountView(APIView):
    """
    システム管理者用アカウント作成View
    """
    authentication_classes = [SystemAdminCreateAccount]

    def post(self, request, *args, **kwargs):
        return Response({"request": "data"}, status=status.HTTP_201_CREATED)


class SystemAdminDeleteAccountView(APIView):
    """
    システム管理者用アカウント削除View
    """
    permission_classes = [IsAuthenticated]
    authentication_classes = [SystemAdminDeleteAccount]

    def post(self, request, *args, **kwargs):
        return Response({"request": "data"}, status=status.HTTP_204_NO_CONTENT)
