# Generated by Django 2.0 on 2019-08-15 15:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('produce', '0006_producetypetwo'),
    ]

    operations = [
        migrations.AddField(
            model_name='produce',
            name='produce_type_two',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='produce.ProduceTypeTwo'),
        ),
    ]
