# Generated by Django 5.0.1 on 2024-06-15 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Server', '0012_careerpath_describition_alter_careerpath_paths'),
    ]

    operations = [
        migrations.AlterField(
            model_name='careerpath',
            name='Paths',
            field=models.CharField(choices=[('penetraion testing', 'Penetraion Testing'), ('blue teaming', 'Blue Teaming'), ('red teaming', 'Rlue Teaming')], max_length=50),
        ),
    ]