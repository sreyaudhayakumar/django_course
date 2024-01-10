# Generated by Django 4.2.3 on 2024-01-09 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0004_delete_passwordchange'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='additional_info',
            field=models.CharField(default=1.11, max_length=10000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='course',
            name='amount',
            field=models.DecimalField(decimal_places=2, default=12.0, max_digits=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='course',
            name='status',
            field=models.CharField(choices=[('Enable', 'Enable'), ('Disable', 'Disable')], default=1, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='course',
            name='subtitle',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]