# Generated by Django 3.2.6 on 2021-10-13 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0007_delete_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='OdiAllrounderRankings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rank', models.IntegerField()),
                ('player', models.CharField(max_length=80)),
                ('country', models.CharField(max_length=80)),
                ('points', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='OdiBattingRankings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rank', models.IntegerField()),
                ('player', models.CharField(max_length=80)),
                ('country', models.CharField(max_length=80)),
                ('points', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='OdiBowlingRankings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rank', models.IntegerField()),
                ('player', models.CharField(max_length=80)),
                ('country', models.CharField(max_length=80)),
                ('points', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='OdiTeamRankings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rank', models.IntegerField()),
                ('country', models.CharField(max_length=80)),
                ('points', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='TallrounderRankings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rank', models.IntegerField()),
                ('player', models.CharField(max_length=80)),
                ('country', models.CharField(max_length=80)),
                ('points', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='TbattingRankings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rank', models.IntegerField()),
                ('player', models.CharField(max_length=80)),
                ('country', models.CharField(max_length=80)),
                ('points', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='TbowlingRankings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rank', models.IntegerField()),
                ('player', models.CharField(max_length=80)),
                ('country', models.CharField(max_length=80)),
                ('points', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='TestAllrounderRankings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rank', models.IntegerField()),
                ('player', models.CharField(max_length=80)),
                ('country', models.CharField(max_length=80)),
                ('points', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='TestBowlingRankings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rank', models.IntegerField()),
                ('player', models.CharField(max_length=80)),
                ('country', models.CharField(max_length=80)),
                ('points', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='TestTeamRankings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rank', models.IntegerField()),
                ('country', models.CharField(max_length=80)),
                ('points', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='TRankings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rank', models.IntegerField()),
                ('country', models.CharField(max_length=80)),
                ('points', models.IntegerField()),
            ],
        ),
    ]
