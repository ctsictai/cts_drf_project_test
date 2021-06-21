# Generated by Django 3.2.4 on 2021-06-21 03:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('sub_title', models.CharField(blank=True, max_length=200, null=True)),
                ('read_cnt', models.IntegerField(default=0)),
                ('writer', models.CharField(blank=True, max_length=100, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('context', models.CharField(blank=True, max_length=1000, null=True)),
            ],
        ),
    ]
