# Generated by Django 2.0 on 2019-08-15 13:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('produce', '0003_programetype'),
    ]

    operations = [
        migrations.AddField(
            model_name='produce',
            name='programe_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='produce.ProgrameType'),
        ),
    ]
