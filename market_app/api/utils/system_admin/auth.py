
import jwt
from rest_framework.authentication import BaseAuthentication
from rest_framework import exceptions

from shop_environ import SECRET_KEY
from api.models import SystemAdminInformation
from api.utils.common import create_request_to_dict, get_timeout_time, date_time
from api.utils.common import create_id, create_password, checked_password


class SystemAdminAuthentication(BaseAuthentication):
    def authenticate(self, request):
        """
        管理者のログイントークンの生成
        :param request: リクエスト
        :return: トークン, None
        """
        header, body = create_request_to_dict(request)

        _id = body["id"]
        password = body["password"]

        user = SystemAdminInformation.objects.filter(id=_id).first()

        if not user:
            raise exceptions.AuthenticationFailed('認証失敗')
        elif user.is_deleted:
            raise exceptions.AuthenticationFailed('削除されたアカウントです')
        elif checked_password(user.password, password):
            raise exceptions.AuthenticationFailed('パスワードあってません')

        token = self.__generate_jwt(user)

        return token, None

    @staticmethod
    def __generate_jwt(system_admin):
        """
        DB情報を元にアクセスTokenを生成する。
        :param system_admin: system_adminのDBのレコードオブジェクト
        :return: JWTの文字列
        """
        return jwt.encode(
            payload={
                "id": system_admin.id,
                "create": str(system_admin.created_at),
                "exp": get_timeout_time()
            },
            key=SECRET_KEY
        ).decode("utf-8")


class SystemAdminCreateAccount(BaseAuthentication):
    def authenticate(self, request):
        """
        システム管理者のアカウント発行
        :param request: リクエストデータ
        :return:
        """
        header, body = create_request_to_dict(request)

        is_created = True
        created_id = None
        while is_created:
            # TODO: ロジックを修正する必要あり。
            # IDがかぶらないものを選択
            created_id = create_id()
            is_created = True if SystemAdminInformation.objects.filter(id=created_id).first() else False

        system_admin_information = SystemAdminInformation()
        system_admin_information.id = created_id
        system_admin_information.password = create_password(body["password"])
        system_admin_information.created_at = date_time()
        system_admin_information.is_deleted = False
        system_admin_information.save()


class SystemAdminJWTAuthentication(BaseAuthentication):
    def authenticate(self, request):
        """
        JWT内のデータの整合性のチェックを行い、アクセス権の確認を行う
        rest_framework.authentication.TokenAuthentication を参考に作成
        :param request:
        :return:
        """
        header, body = create_request_to_dict(request)
        auth_info = header["HTTP_AUTHORIZATION"]

        if not auth_info:
            # Tokenが含まれていない場合
            raise exceptions.AuthenticationFailed("認証情報が不正です。")
        if len(auth_info.split(".")) != 3:
            raise exceptions.AuthenticationFailed("認証情報が不正です。")

        jwt_header = jwt.get_unverified_header(auth_info)
        jwt_payload = jwt.decode(auth_info, SECRET_KEY)

        if jwt_header["typ"] != "JWT" and jwt_header["alg"] != "HS256":
            # JWT以外のタイプとHS256以外の形式を受け付けない
            raise exceptions.AuthenticationFailed("認証情報が不正です。")
        if jwt_payload is None:
            raise exceptions.AuthenticationFailed("認証情報が不正です。")

        try:
            user = SystemAdminInformation.objects.filter(id=jwt_payload["id"]).first()
            user.is_authenticated = True

            return user, auth_info

        except Exception as e:
            raise exceptions.AuthenticationFailed("認証情報が不正です。")


class SystemAdminDeleteAccount(BaseAuthentication):
    def authenticate(self, request):
        header, body = create_request_to_dict(request)

        _id = body["id"]
        password = body["password"]

        system_admin_information = SystemAdminInformation.objects.filter(id=_id).first()

        if checked_password(system_admin_information.password, password):
            raise exceptions.AuthenticationFailed("認証情報が不正です。")

        try:
            system_admin_information.deleted_at = date_time()
            system_admin_information.is_deleted = True
            system_admin_information.save()

        except Exception as e:
            raise e






