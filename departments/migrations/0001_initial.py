# Generated by Django 4.2.4 on 2023-11-22 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Departments',
            fields=[
                ('departmentid', models.AutoField(db_column='DepartmentID', primary_key=True, serialize=False)),
                ('named', models.CharField(blank=True, db_column='NameD', max_length=50, null=True)),
            ],
            options={
                'db_table': 'departments',
                'permissions': [('can_manage_departments', 'Can manage departments')],
                'managed': False,
            },
        ),
    ]
