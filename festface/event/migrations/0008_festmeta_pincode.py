# Generated by Django 2.0 on 2018-09-27 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0007_auto_20180927_1947'),
    ]

    operations = [
        migrations.AddField(
            model_name='festmeta',
            name='pincode',
            field=models.CharField(default='534007', max_length=6),
            preserve_default=False,
        ),
    ]
