# Generated by Django 4.1.3 on 2022-12-17 03:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("dashboard", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="JadwalSholat",
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
                ("idsholat", models.CharField(blank=True, max_length=225, null=True)),
                ("lokasi", models.CharField(blank=True, max_length=225, null=True)),
                ("subuh", models.CharField(blank=True, max_length=225, null=True)),
                ("zuhur", models.CharField(blank=True, max_length=225, null=True)),
                ("asar", models.CharField(blank=True, max_length=225, null=True)),
                ("maghrib", models.CharField(blank=True, max_length=225, null=True)),
                ("isya", models.CharField(blank=True, max_length=225, null=True)),
            ],
        ),
    ]
