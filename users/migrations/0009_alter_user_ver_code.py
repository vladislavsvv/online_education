# Generated by Django 5.0 on 2024-01-02 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_alter_user_ver_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='ver_code',
            field=models.CharField(default='171290533163', max_length=15, verbose_name='Проверочный код'),
        ),
    ]
