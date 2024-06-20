from django.core.validators import MinLengthValidator, RegexValidator
from django.db import models

from user_profile.models import Profile

LAT_LNG_REGEX = r"^-?\d{1,3}(\.\d{1,20})?$"


class Address(models.Model):
    latitude = models.CharField(
        max_length=25,
        validators=[
            RegexValidator(
                regex=LAT_LNG_REGEX,
                message="عدد اعشاری الزامی است",
            )
        ],
    )
    longitude = models.CharField(
        max_length=25,
        validators=[
            RegexValidator(
                regex=LAT_LNG_REGEX,
                message="عدد اعشاری الزامی است",
            )
        ],
    )
    title = models.CharField(max_length=120)
    description = models.TextField()
    mobile = models.CharField(max_length=11, validators=[MinLengthValidator(11)])
    owner = models.ForeignKey(Profile, on_delete=models.PROTECT, editable=False)

    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        db_table = "address"
