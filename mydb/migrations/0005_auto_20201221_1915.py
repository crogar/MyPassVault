# Generated by Django 3.1.4 on 2020-12-22 00:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mydb', '0004_account_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='comment',
            field=models.CharField(max_length=1500),
        ),
        migrations.AlterField(
            model_name='account',
            name='url',
            field=models.URLField(),
        ),
    ]
