from django.db import models
from django.utils import timezone
from datetime import date


# Create your models here.
class Testruns(models.Model):
    name=models.CharField(max_length=250,unique=True)
    country=models.CharField(max_length=100)
    matches=models.IntegerField(null=True)
    runs_scored=models.IntegerField()
    high_score=models.IntegerField(null=True)
    hundreds=models.IntegerField()
    fifties=models.IntegerField()


class Odiruns(models.Model):
    name=models.CharField(max_length=250,unique=True)
    country=models.CharField(max_length=100)
    runs_scored=models.IntegerField()
    high_score=models.IntegerField()
    hundreds=models.IntegerField()
    fifties=models.IntegerField()



class Truns(models.Model):
    name=models.CharField(max_length=250,unique=True)
    country=models.CharField(max_length=100)
    matches=models.IntegerField()
    runs_scored=models.IntegerField()
    high_score=models.IntegerField()
    hundreds=models.IntegerField()
    fifties=models.IntegerField()


class Testbal(models.Model):
    name=models.CharField(max_length=250,unique=True)
    country=models.CharField(max_length=100)
    matches=models.IntegerField()
    wickets=models.IntegerField()
    econamy=models.DecimalField(max_digits=3,decimal_places=2)
class Odibal(models.Model):
    name=models.CharField(max_length=250,unique=True)
    country=models.CharField(max_length=100)
    matches=models.IntegerField()
    wickets=models.IntegerField()
    econamy=models.DecimalField(max_digits=3,decimal_places=2)

class Format(models.Model):
    name=models.CharField(max_length=250,unique=True)
    country=models.CharField(max_length=100)
    matches=models.IntegerField()
    wickets=models.IntegerField()
    econamy=models.DecimalField(max_digits=3,decimal_places=2)


class Comment(models.Model):
    name = models.CharField(max_length=80,null=True)
    email = models.EmailField()
    body = models.TextField(default='', blank=True)
    date = models.DateTimeField(default=timezone.now)

class TestRankings(models.Model):
    rank=models.IntegerField()
    player=models.CharField(max_length=80)
    country=models.CharField(max_length=80)
    points=models.IntegerField()


class TestTeamRankings(models.Model):
    rank=models.IntegerField()
    country=models.CharField(max_length=80)
    points=models.IntegerField()


class TestBowlingRankings(models.Model):
    rank=models.IntegerField()
    player=models.CharField(max_length=80)
    country=models.CharField(max_length=80)
    points=models.IntegerField()


class TestAllrounderRankings(models.Model):
    rank=models.IntegerField()
    player=models.CharField(max_length=80)
    country=models.CharField(max_length=80)
    points=models.IntegerField()

class OdiTeamRankings(models.Model):
    rank=models.IntegerField()
    country=models.CharField(max_length=80)
    points=models.IntegerField()


class OdiBattingRankings(models.Model):
    rank=models.IntegerField()
    player=models.CharField(max_length=80)
    country=models.CharField(max_length=80)
    points=models.IntegerField()


class OdiBowlingRankings(models.Model):
    rank=models.IntegerField()
    player=models.CharField(max_length=80)
    country=models.CharField(max_length=80)
    points=models.IntegerField()


class OdiAllrounderRankings(models.Model):
    rank=models.IntegerField()
    player=models.CharField(max_length=80)
    country=models.CharField(max_length=80)
    points=models.IntegerField()

class TRankings(models.Model):
    rank=models.IntegerField()
    country=models.CharField(max_length=80)
    points=models.IntegerField()


class TbattingRankings(models.Model):
    rank=models.IntegerField()
    player=models.CharField(max_length=80)
    country=models.CharField(max_length=80)
    points=models.IntegerField()


class TbowlingRankings(models.Model):
    rank=models.IntegerField()
    player=models.CharField(max_length=80)
    country=models.CharField(max_length=80)
    points=models.IntegerField()


class TallrounderRankings(models.Model):
    rank=models.IntegerField()
    player=models.CharField(max_length=80)
    country=models.CharField(max_length=80)
    points=models.IntegerField()


class TeamsImages(models.Model):
    sno=models.IntegerField()
    country=models.CharField(max_length=80)
    logo=models.FileField(upload_to='uploads/')