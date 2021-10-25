from django.shortcuts import render
from web.forms import TestrunsForm
from web.models import *
from django import forms
from datetime import datetime



# Create your views here.
#def rupesh(request):
 #   return render(request,'web/rupesh.html')
def Teams(request):
    tm=TeamsImages.objects.all
    return render(request,'web/Teams.html',{'access_records':tm})
def Players(request):
    return render(request,'web/Players.html')

def Rankings(request):
    return render(request,'web/Rankings.html')
def Stats(request):
    return render(request,'web/Stats.html')
def Records(request):
    return render(request,'web/Records.html')
def IPL(request):
    return render(request,'web/IPL.html') 
    

def india(request):
    return render(request,'web/india.html') 
def australia(request):
    return render(request,'web/australia.html') 
def southafrica(request):
    return render(request,'web/southafrica.html') 
def westindies(request):
    return render(request,'web/westindies.html') 
def england(request):
    return render(request,'web/england.html') 
def newzland(request):
    return render(request,'web/newzland.html') 
def srilanka(request):
    return render(request,'web/srilanka.html') 
def irland(request):
    return render(request,'web/irland.html') 
def pak(request):
    return render(request,'web/pak.html') 
def afgan(request):
    return render(request,'web/afgan.html') 
def zimbawe(request):
    return render(request,'web/zimbawe.html') 
def bangaladesh(request):
    return render(request,'web/bangaladesh.html')



def all(request):
    return render(request,'web/all.html') 
def bowling(request):
    return render(request,'web/bowling.html') 
def batting(request):
 #   obj=Testruns.objects.all
    return render(request,'web/batting.html') 
def test(request):
    ban=Testruns.objects.all
    return render(request,'web/test.html',{'access_records':ban})
def odi(request):
    gal=Odiruns.objects.all
    return render(request,'web/odi.html',{'access_records':gal}) 
def twinty(request):
    two=Truns.objects.all
    return render(request,'web/twinty.html',{'access_records':two}) 
def hit(request):
    an=Testbal.objects.all
    return render(request,'web/testbowling.html',{'access_records':an})
def wicket(request):
    dh=Odibal.objects.all
    return render(request,'web/odibowling.html',{'access_records':dh}) 
def stumps(request):
    ra=Format.objects.all
    return render(request,'web/twintybowling.html',{'access_records':ra}) 


def icc_test(request):
    return render(request,'web/icc_test.html') 
def icc_odi(request):
    return render(request,'web/icc_odi.html')
def icct20(request):
    return render(request,'web/icct20.html') 
def icc_test_team(request):
    de=TestTeamRankings.objects.all
    return render(request,'web/icc_test_team.html',{'access_records':de})
def icc_testbatting_team(request):
    si=TestRankings.objects.all
    return render(request,'web/icc_testbatting_team.html',{'access_records':si}) 
def icc_testbowling_team(request):
    re=TestBowlingRankings.objects.all
    return render(request,'web/icc_testbowling_team.html',{'access_records':re})
def icc_testallrounder_team(request):
    ddy=TestAllrounderRankings.objects.all
    return render(request,'web/icc_testallrounder_team.html',{'access_records':ddy}) 
def icc_odi_team(request):
    bh=OdiTeamRankings.objects.all
    return render(request,'web/icc_odi_team.html',{'access_records':bh})
def icc_odibatting_team(request):
    us=OdiBattingRankings.objects.all
    return render(request,'web/icc_odibatting_team.html',{'access_records':us}) 
def icc_odibowling_team(request):
    sh=OdiBowlingRankings.objects.all
    return render(request,'web/icc_odibowling_team.html',{'access_records':sh})
def icc_odiallrounder_team(request):
    an=OdiAllrounderRankings.objects.all
    return render(request,'web/icc_odiallrounder_team.html',{'access_records':an}) 
def icc_t20_team(request):
    ku=TRankings.objects.all
    return render(request,'web/icc_t20_team.html',{'access_records':ku})
def icc_t20batting_team(request):
    ma=TbattingRankings.objects.all
    return render(request,'web/icc_t20batting_team.html',{'access_records':ma}) 
def icc_t20bowling_team(request):
    ar=TbowlingRankings.objects.all
    return render(request,'web/icc_t20bowling_team.html',{'access_records':ar})
def icc_t20allrounder_team(request):
    bs=TallrounderRankings.objects.all
    return render(request,'web/icc_t20allrounder_team.html',{'access_records':bs}) 

#def fifties(request):
    #return render(request,'web/fifties.html') 
#def test_mostrun(request):
    #return render(request,'web/test_mostrun.html') 
#def test_mostrun(request):
 #   obj=Testruns.objects.all()
  #  return render(request,'web/Test_
#def dhoni(request):
    #Comment = get_object  #_or_404(Post, pk=pk)
    # post = Post

 #   if request.method == "POST":
  #      form = CommentForm(request.POST)
   #     if form.is_valid():
    #        comment = form.save(commit=False)
     #       print("............")
      #      comment.form=save
       #     print("...............3")
        #    comment.save()

    #else:
     #   form = CommentForm()
    #return render(req6uest, 'web/dhoni.html', {'form': form})

'''def dhoni(request):
    #registered=False
    if request.method=='POST':
        form=Comment.objects.all()
        
            comm = Comment()
            comm.name = name
            comm.email_id = email_id
            comm.body = body
            comm.date = date.today()
        
            comment.save()
    else:
        form = Comment()
    return render(request,'web/dhoni.html', {'form': form})'''
def rupesh(request):

    form= Comment.objects.all()
    if request.method =='POST':
        name = request.POST.get("username")
        email = request.POST.get("email")
        body = request.POST.get("body")
        c = Comment()
        c.name = name
        c.email = email
        c.body = body
        c.date = date.today()
        c.save()
    return render(request,"web/rupesh.html",{'access_rec':form})
    