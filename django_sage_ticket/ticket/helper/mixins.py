import secrets

from django.utils.translation import gettext_lazy as _
from django.db import models

from django.core.validators import MaxLengthValidator, MinLengthValidator


class SKUMixin(models.Model):
    sku = models.CharField(
        _("SKU"),
        max_length=50,
        unique=True,
        editable=False,
        default=secrets.token_urlsafe,
        validators=[
            MaxLengthValidator(50),
        ],
        help_text=_(
            "An alternate field to store the unique identity per object."
            " This field is also shown in the URL."
        ),
    )

    class Meta:
        abstract = True


class TitleSlugMixin(models.Model):
    title = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(_("Slug"), unique=True)

    class Meta:
        abstract = True


class TitleMixin(models.Model):
    title = models.CharField(
        max_length=255,
    )

    class Meta:
        abstract = True


class TimeStampMixin(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class UploadBasePictureMixin(models.Model):
    picture = models.ImageField(
        _("picture"),
        upload_to="media/uploads",
        width_field="width_field",
        height_field="height_field",
        help_text=_("The picture that is uploaded."),
    )
    alternate_text = models.CharField(
        _("Alternate Text"),
        max_length=250,
        null=True,
        validators=[MaxLengthValidator(110), MinLengthValidator(10)],
        help_text=_(
            "Describe the picture that is uploaded." "search engine optimization"
        ),
    )
    width_field = models.PositiveIntegerField(
        _("width field"), editable=False, null=True, help_text=_("The Picture's width.")
    )
    height_field = models.PositiveIntegerField(
        _("Height Field"),
        editable=False,
        null=True,
        help_text=_("The picture's height."),
    )

    class Meta:
        abstract = True
