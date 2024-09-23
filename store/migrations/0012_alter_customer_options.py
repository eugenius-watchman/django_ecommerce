# Generated by Django 5.1.1 on 2024-09-20 18:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("store", "0011_alter_order_options_customer_phone"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="customer",
            options={
                "ordering": ["user__first_name", "user__last_name"],
                "permissions": [("view_history", "Can view history")],
            },
        ),
    ]
