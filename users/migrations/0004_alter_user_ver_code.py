# Generated by Django 5.0 on 2023-12-09 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_user_ver_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='ver_code',
            field=models.CharField(default='851978720568', max_length=15, verbose_name='Проверочный код'),
        ),
    ]
