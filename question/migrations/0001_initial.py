# Generated by Django 2.0 on 2019-08-15 04:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Choise',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('c1', models.CharField(max_length=100)),
                ('v1', models.IntegerField(default=0)),
                ('c2', models.CharField(max_length=100)),
                ('v2', models.IntegerField(default=0)),
                ('c3', models.CharField(max_length=100)),
                ('v3', models.IntegerField(default=0)),
                ('c4', models.CharField(max_length=100)),
                ('v4', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='choise',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='question.Question'),
        ),
    ]
