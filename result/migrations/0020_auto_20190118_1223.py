# Generated by Django 2.1.2 on 2019-01-18 12:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('result', '0019_auto_20190117_1631'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='courseallocation',
            name='session',
        ),
        migrations.AddField(
            model_name='courseallocation',
            name='semester',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='result.Semester'),
        ),
    ]
