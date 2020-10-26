import time
import json
import uuid
from django.contrib.auth.hashers import make_password, check_password
from datetime import datetime


def get_timeout_time():
    """
    セッションのタイムアウトする時間を返却
    :return: int(UnixTime) + 7日
    """
    return int(time.time()) + 60*60*24*7


def date_time():
    """
    全ての箇所で利用される日付の参照元
    時間フォーマット: YYYY/MM/DD hh:mm:ss+0000
    settings.pyでTimeZoneがAsia/Tokyoになっているので
    タイムゾーンを0000で指定する必要がある。
    ずれる場合は、乗せるマシンを調整する必要がある。
    :return: 時刻
    """
    return datetime.strftime(datetime.now(), "%Y-%m-%d %H:%M:%S+0000")


def create_request_to_dict(request):
    """
    リクエストのheader(META), BodyデータをJsonに変換
    METAデータはDictで受け取るのでそのまま返却する
    :param request: リクエストデータ
    :return: header, body
    """
    header = request.META
    if request.body:
        body = json.loads(request.body)
    else:
        body = dict()
    return header, body


def create_id():
    """
    全てのIDの発行
    :return: uuid(v4)
    """
    return uuid.uuid4()


def create_password(password):
    """
    全てのアカウントのパスワードを発行する
    :param password: 送られたきたパスワード
    :return: 暗号化されたパスワード
    """
    return make_password(password)


def checked_password(password, registered_password):
    """
    全てのアカウントのパスワードのチェックを行う
    :param password: ボディに含まれているパスワード
    :param registered_password: DBに登録されているパスワード
    :return: 真偽値
    """
    return check_password(password, registered_password)
