# Generated by Django 5.0.1 on 2024-01-13 04:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_alter_user_ver_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='ver_code',
            field=models.CharField(default='012531221946', max_length=15, verbose_name='Проверочный код'),
        ),
    ]
