# Generated by Django 5.0.3 on 2024-04-24 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='type',
            field=models.CharField(choices=[('Bachelor', 'Bachelor'), ('Master', 'Master')], default='Bachelor', max_length=16),
        ),
    ]
