# Generated by Django 2.0 on 2019-08-14 09:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produce',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('price', models.FloatField(max_length=50)),
                ('content', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='produce', verbose_name='产品图片')),
                ('information_image', models.ImageField(upload_to='produce', verbose_name='产品介绍图片')),
                ('information', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ProduceType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='produce',
            name='produce_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='produce.ProduceType'),
        ),
    ]
