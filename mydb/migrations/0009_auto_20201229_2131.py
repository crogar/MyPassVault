# Generated by Django 3.1.4 on 2020-12-30 02:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mydb', '0008_auto_20201229_2130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=50),
        ),
    ]