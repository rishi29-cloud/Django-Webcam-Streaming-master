# Generated by Django 3.2 on 2022-05-22 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='vehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vehicle_no', models.CharField(blank=True, max_length=255, null=True)),
                ('color', models.CharField(blank=True, max_length=255, null=True)),
                ('model', models.CharField(blank=True, max_length=255, null=True)),
                ('year', models.CharField(blank=True, max_length=255, null=True)),
                ('created_by', models.CharField(blank=True, max_length=255, null=True)),
                ('created_dt', models.DateTimeField(auto_now_add=True)),
                ('updated_by', models.CharField(blank=True, max_length=255, null=True)),
                ('updated_dt', models.DateTimeField(auto_now=True)),
                ('deleted', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
    ]
