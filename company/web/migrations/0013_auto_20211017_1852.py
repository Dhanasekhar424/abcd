# Generated by Django 3.2.6 on 2021-10-17 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0012_rename_teams_teamsimages'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('email', models.EmailField(max_length=254)),
                ('body', models.TextField(blank=True, default='')),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AlterField(
            model_name='teamsimages',
            name='logo',
            field=models.ImageField(default='default', upload_to=None),
        ),
    ]
