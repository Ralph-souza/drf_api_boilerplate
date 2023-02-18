from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class UsersConfig(AppConfig):
    name = "drf_api_boilerplate.users"
    verbose_name = _("Users")

    def ready(self):
        try:
            import drf_api_boilerplate.users.signals  # noqa F401
        except ImportError:
            pass
