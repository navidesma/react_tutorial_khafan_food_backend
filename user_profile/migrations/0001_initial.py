# Generated by Django 4.2.13 on 2024-06-24 08:26

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import user_profile.models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Profile",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("first_name", models.CharField(max_length=256)),
                ("last_name", models.CharField(max_length=256)),
                (
                    "mobile",
                    models.CharField(
                        max_length=11,
                        validators=[django.core.validators.MinLengthValidator(11)],
                    ),
                ),
                (
                    "type",
                    models.CharField(
                        choices=[
                            (
                                user_profile.models.UserType["RESTAURANT_OWNER"],
                                "RESTAURANT_OWNER",
                            ),
                            (
                                user_profile.models.UserType["NORMAL_USER"],
                                "NORMAL_USER",
                            ),
                        ],
                        max_length=64,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "db_table": "profile",
            },
        ),
    ]