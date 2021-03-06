# Generated by Django 2.0 on 2020-05-30 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0002_auto_20200530_1822'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='trending',
            options={'ordering': ['order'], 'verbose_name': 'Trending', 'verbose_name_plural': 'Trendings'},
        ),
        migrations.AddField(
            model_name='trending',
            name='image',
            field=models.ImageField(default=1, upload_to='images/trending', verbose_name='Image'),
            preserve_default=False,
        ),
    ]
