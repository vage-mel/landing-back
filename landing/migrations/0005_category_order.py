# Generated by Django 2.0 on 2020-05-30 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0004_auto_20200530_1838'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='order',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
    ]