# Generated by Django 2.0 on 2018-09-27 13:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0004_registrations'),
    ]

    operations = [
        migrations.AddField(
            model_name='events',
            name='festname',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, related_name='fest_event', to='event.Festmeta'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='festmeta',
            name='college',
            field=models.CharField(default='null', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='festmeta',
            name='collegewebstite',
            field=models.CharField(default='null', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='festmeta',
            name='festmail',
            field=models.CharField(default='null', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='festmeta',
            name='spocmail1',
            field=models.CharField(default='null', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='festmeta',
            name='spocmail2',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='festmeta',
            name='spocname1',
            field=models.CharField(default='null', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='festmeta',
            name='spocname2',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='festmeta',
            name='spocphone1',
            field=models.CharField(default='null', max_length=14),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='festmeta',
            name='spocphone2',
            field=models.CharField(blank=True, max_length=14, null=True),
        ),
        migrations.AlterField(
            model_name='events',
            name='short_desc',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='festmeta',
            name='registration_fee',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='festmeta',
            name='venue',
            field=models.CharField(max_length=200),
        ),
    ]
