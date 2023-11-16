# Generated by Django 4.2.6 on 2023-11-16 06:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Asset",
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
                ("name", models.CharField(max_length=128)),
                (
                    "description",
                    models.CharField(blank=True, default="", max_length=255, null=True),
                ),
                ("asset_code", models.CharField(max_length=128, unique=True)),
                ("asset_model_number", models.CharField(max_length=128)),
                ("asset_serial_number", models.CharField(default="", max_length=128)),
                ("asset_purchase_date", models.DateField()),
                ("modified_on", models.DateField(auto_now=True)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("OPERATIONAL", "Operational"),
                            ("NONOPERATIONAL", "Nonoperational"),
                            ("MISSING", "Missing"),
                        ],
                        default="OPERATIONAL",
                        max_length=128,
                    ),
                ),
            ],
            options={
                "verbose_name": "Asset",
                "verbose_name_plural": "Assets",
            },
        ),
        migrations.CreateModel(
            name="AssetGroup",
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
                ("name", models.CharField(max_length=128, unique=True)),
                (
                    "description",
                    models.CharField(blank=True, default="", max_length=255, null=True),
                ),
            ],
            options={
                "verbose_name": "Asset Group",
                "verbose_name_plural": "Asset Groups",
            },
        ),
        migrations.CreateModel(
            name="AssetAllocation",
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
                ("employee_name", models.CharField(default="Office", max_length=255)),
                (
                    "asset",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="asset_management.asset",
                    ),
                ),
            ],
            options={
                "verbose_name": "Asset Allocation",
                "verbose_name_plural": "Asset Allocations",
            },
        ),
        migrations.AddField(
            model_name="asset",
            name="asset_group",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="assets",
                to="asset_management.assetgroup",
            ),
        ),
    ]