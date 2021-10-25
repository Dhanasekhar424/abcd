from django import forms
#from django.contrib.auth.models import User
#from login_app.models import UserProfileInfo
#from login_app.models import Flip
#from web.models import date
from web.models import Testruns,Odiruns,Truns,Testbal,Odibal,Format,TestRankings,TestTeamRankings,TestBowlingRankings,TestAllrounderRankings,OdiTeamRankings,OdiBattingRankings,OdiBowlingRankings,OdiAllrounderRankings,TRankings,TbattingRankings,TbowlingRankings,TallrounderRankings,TeamsImages,Comment
class TestrunsForm(forms.ModelForm):
    name=forms.CharField()
    country=forms.CharField()
    matches=forms.IntegerField()
    runs_scored=forms.IntegerField()
    high_score=forms.IntegerField()
    hundreds=forms.IntegerField()
    fifties=forms.IntegerField()
    class Meta():
        model=Testruns
        fields="__all__"


class OdirunsForm(forms.ModelForm):
    name=forms.CharField()
    country=forms.CharField()
    matches=forms.IntegerField()
    runs_scored=forms.IntegerField()
    high_score=forms.IntegerField()
    hundreds=forms.IntegerField()
    fifties=forms.IntegerField()
    class Meta():
        model=Odiruns
        fields="__all__"

    

class TrunsForm(forms.ModelForm):  
    name=forms.CharField()
    country=forms.CharField()
    matches=forms.IntegerField()
    runs_scored=forms.IntegerField()
    high_score=forms.IntegerField()
    hundreds=forms.IntegerField()
    fifties=forms.IntegerField()
    class Meta():
        model=Truns
        fields="__all__"  



class TestbalForm(forms.ModelForm):  
    name=forms.CharField()
    country=forms.CharField()
    matches=forms.IntegerField()
    wickets=forms.IntegerField()
    econamy=forms.DecimalField()
    class Meta():
        model=Testbal
        fields="__all__"  

class OdibalForm(forms.ModelForm):  
    name=forms.CharField()
    country=forms.CharField()
    matches=forms.IntegerField()
    wickets=forms.IntegerField()
    econamy=forms.DecimalField()
    class Meta():
        model=Odibal
        fields="__all__"  

class FormatForm(forms.ModelForm):  
    name=forms.CharField()
    country=forms.CharField()
    wickets=forms.IntegerField()
    conamy=forms.DecimalField()
    class Meta():
        model=Format
        fields="__all__"  
#class CommentForm(forms.ModelForm):
 #   name=forms.CharField()
  #  email=forms.EmailField()
    #add your comments here=forms.CharField()
    
class CommentForm(forms.ModelForm):
    #name=forms.CharField()
    #email=forms.EmailField()
    #body=forms.TextField()
    #date=forms.DateTimeField()
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body','date')
class TestRankingsForm(forms.ModelForm):
    class Meta:
        Model=TestRankings
        fields=('rank','player','country','points')

class TestTeamRankingsForm(forms.ModelForm):
    class Meta:
        Model=TestTeamRankings
        fields=('rank','country','points')


class TestBowlingRankingsForm(forms.ModelForm):
    class Meta:
        Model=TestBowlingRankings
        fields=('rank','player','country','points')

class TestAllrounderRankingsForm(forms.ModelForm):
    class Meta:
        Model=TestAllrounderRankings
        fields=('rank','player','country','points')

class OdiTeamRankingsForm(forms.ModelForm):
    class Meta:
        Model=OdiTeamRankings
        fields=('rank','country','points')

class OdiBattingRankingsForm(forms.ModelForm):
    class Meta:
        Model=OdiBattingRankings
        fields=('rank','player','country','points')


class OdiBowlingRankingsForm(forms.ModelForm):
    class Meta:
        Model=OdiBowlingRankings
        fields=('rank','player','country','points')

class OdiAllrounderRankingsForm(forms.ModelForm):
    class Meta:
        Model=OdiAllrounderRankings
        fields=('rank','player','country','points')

class TRankingsForm(forms.ModelForm):
    class Meta:
        Model=TRankings
        fields=('rank','country','points')

class TbattingRankingsForm(forms.ModelForm):
    class Meta:
        Model=TbattingRankings
        fields=('rank','player','country','points')

class TbowlingRankingsForm(forms.ModelForm):
    class Meta:
        Model=TbowlingRankings
        fields=('rank','player','country','points')

class TallrounderRankingsForm(forms.ModelForm):
    class Meta:
        Model=TallrounderRankings
        fields=('rank','player','country','points')


class TeamsImagesForm(forms.ModelForm):
    class Meta:
        Model=TeamsImages
        fields=('sno','country','logo')


