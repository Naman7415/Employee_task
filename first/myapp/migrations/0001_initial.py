# Generated by Django 5.0.4 on 2024-04-15 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="EmployeeModel",
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
                (
                    "EmployeeName",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                (
                    "EmployeeEmail",
                    models.EmailField(
                        blank=True, max_length=100, null=True, unique=True
                    ),
                ),
                ("EmployeePanNumber", models.IntegerField(null=True)),
                ("EmployeeMobileNumber", models.IntegerField(blank=True, null=True)),
                ("EmployeeSalary", models.IntegerField(null=True)),
            ],
        ),
    ]