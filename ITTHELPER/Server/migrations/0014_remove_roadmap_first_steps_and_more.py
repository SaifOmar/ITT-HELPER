# Generated by Django 5.0.1 on 2024-06-15 06:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Server', '0013_alter_careerpath_paths'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='roadmap',
            name='first_steps',
        ),
        migrations.RemoveField(
            model_name='roadmap',
            name='fourth_steps',
        ),
        migrations.RemoveField(
            model_name='roadmap',
            name='second_steps',
        ),
        migrations.RemoveField(
            model_name='roadmap',
            name='third_steps',
        ),
        migrations.AddField(
            model_name='roadmap',
            name='html_file',
            field=models.CharField(default='', max_length=250),
        ),
        migrations.AlterField(
            model_name='careerpath',
            name='Paths',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='company',
            name='CompanyName',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='eventsandworkshops',
            name='Deadline',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='eventsandworkshops',
            name='EventDate',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='eventsandworkshops',
            name='EventTime',
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name='roadmap',
            name='path',
            field=models.ForeignKey(default=7, on_delete=django.db.models.deletion.CASCADE, related_name='path', to='Server.careerpath'),
        ),
    ]
