# Generated by Django 4.1.5 on 2023-04-23 08:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('expenses', '0006_alter_saving_created_at'),
    ]

    operations = [
        migrations.RenameField(
            model_name='savingcategory',
            old_name='created_at',
            new_name='created_date',
        ),
    ]