# Generated by Django 3.1.12 on 2025-02-26 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coreApp', '0006_auto_20250226_2110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='depotcases2024',
            name='GISDATE',
            field=models.DateField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='depotcases2024',
            name='MSPDATE',
            field=models.DateField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='depotcases2024',
            name='PASSEDDATE',
            field=models.DateField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='depotcases2024',
            name='RCCDATE',
            field=models.DateField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='depotcases2024',
            name='USPDATE',
            field=models.DateField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='depotcases2025',
            name='GISDATE',
            field=models.DateField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='depotcases2025',
            name='MSPDATE',
            field=models.DateField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='depotcases2025',
            name='PASSEDDATE',
            field=models.DateField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='depotcases2025',
            name='RCCDATE',
            field=models.DateField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='depotcases2025',
            name='USPDATE',
            field=models.DateField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='permit',
            name='passed_date',
            field=models.DateField(blank=True, default='', null=True, verbose_name='Passed Date'),
        ),
        migrations.AlterField(
            model_name='permit',
            name='to_gis_date',
            field=models.DateField(blank=True, default='', null=True, verbose_name='To GIS Date'),
        ),
        migrations.AlterField(
            model_name='permit',
            name='to_wl_date',
            field=models.DateField(blank=True, default='', null=True, verbose_name='To WL Date'),
        ),
    ]
