# Generated by Django 3.2.6 on 2021-10-18 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0017_alter_teamsimages_logo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teamsimages',
            name='logo',
            field=models.ImageField(default='default', upload_to="{ static'images\\css' }"),
        ),
    ]
