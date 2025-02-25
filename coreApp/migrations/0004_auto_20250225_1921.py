# Generated by Django 3.1.12 on 2025-02-25 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coreApp', '0003_auto_20250224_1110'),
    ]

    operations = [
        migrations.RenameField(
            model_name='permit',
            old_name='Block',
            new_name='block',
        ),
        migrations.RenameField(
            model_name='permit',
            old_name='Parcel_Number',
            new_name='parcel_number',
        ),
        migrations.RenameField(
            model_name='permit',
            old_name='PASSED_DATE',
            new_name='passed_date',
        ),
        migrations.RenameField(
            model_name='permit',
            old_name='Plan_Status',
            new_name='plan_status',
        ),
        migrations.RenameField(
            model_name='permit',
            old_name='PlanEng',
            new_name='planeng',
        ),
        migrations.RenameField(
            model_name='permit',
            old_name='REF_NO',
            new_name='ref_no',
        ),
        migrations.RenameField(
            model_name='permit',
            old_name='TO_GIS_DATE',
            new_name='to_gis_date',
        ),
        migrations.RenameField(
            model_name='permit',
            old_name='TO_WL_DATE',
            new_name='to_wl_date',
        ),
        migrations.RenameField(
            model_name='permit',
            old_name='WL_NUMBER',
            new_name='wl_number',
        ),
        migrations.RemoveField(
            model_name='permit',
            name='Area',
        ),
        migrations.RemoveField(
            model_name='permit',
            name='KVA',
        ),
        migrations.RemoveField(
            model_name='permit',
            name='KW',
        ),
        migrations.RemoveField(
            model_name='permit',
            name='Stage',
        ),
        migrations.RemoveField(
            model_name='permit',
            name='Status',
        ),
        migrations.AddField(
            model_name='permit',
            name='kva',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='permit',
            name='kw',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='depotcases2024',
            name='cable_length',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='depotcases2024',
            name='labourcost',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='depotcases2024',
            name='ministrycost',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='depotcases2024',
            name='noOfFaults',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='depotcases2024',
            name='noOfServ',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='depotcases2024',
            name='totalcost',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='depotcases2025',
            name='cable_length',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='depotcases2025',
            name='labourcost',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='depotcases2025',
            name='ministrycost',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='depotcases2025',
            name='noOfFaults',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='depotcases2025',
            name='noOfServ',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='depotcases2025',
            name='totalcost',
            field=models.FloatField(),
        ),
    ]
