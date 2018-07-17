from django.apps import AppConfig


class UsersConfig(AppConfig):
    # 表示这个配置类是加载到哪个应用的，
    # 每个配置类必须包含此属性，默认自动生成
    name = 'users'