# Generated by Django 4.1 on 2022-09-04 19:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Restaurant_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='plat',
            old_name='categorie',
            new_name='platcategorie',
        ),
    ]
