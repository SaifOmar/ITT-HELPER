# Generated by Django 5.0.1 on 2024-06-14 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_customuser_email_is_verified'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='img',
            field=models.ImageField(default='default_user.jpg', upload_to='user-imgaes'),
        ),
    ]