from rest_framework import serializers
# モデルインポート
from .models import SystemAdminInformation
# from .models import SubList

# TODO: 多分要らない。

# メインリストシリアライザ
class MainListSerializer(serializers.ModelSerializer):
    class Meta:
        model = SystemAdminInformation
        # 取得フィールド設定
        fields = (
            "id",
            "password",
            "created_at",
            "deleted_at",
            "is_deleted"
        )


# #サブリストシリアライザ
# class SubListSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = SubList
#         #取得フィールド設定
#         fields = ('title', 'totalnum')
