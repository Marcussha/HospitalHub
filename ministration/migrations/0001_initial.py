# Generated by Django 4.2.4 on 2023-08-25 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ministration',
            fields=[
                ('minisid', models.AutoField(db_column='MinisID', primary_key=True, serialize=False)),
                ('name_ministration', models.CharField(db_column='Name_ministration', max_length=70)),
            ],
            options={
                'db_table': 'ministration',
                'managed': False,
            },
        ),
    ]
