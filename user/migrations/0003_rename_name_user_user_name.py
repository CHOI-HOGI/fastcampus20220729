# Generated by Django 4.0.6 on 2022-07-28 08:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_rename_user_name_user_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='name',
            new_name='user_name',
        ),
    ]
