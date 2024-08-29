from django.conf import settings
from django.core.checks import Error, register


@register()
def check_installed_apps(app_configs, **kwargs):
    errors = []
    required_apps = [
        "sage_ticket",
    ]

    for app in required_apps:
        if app not in settings.INSTALLED_APPS:
            errors.append(
                Error(
                    f"'{app}' is missing in INSTALLED_APPS.",
                    hint=f"Add '{app}' to INSTALLED_APPS in your settings.",
                    obj=settings,
                    id=f"sage_invoice.E00{required_apps.index(app) + 1}",
                )
            )

    return errors
