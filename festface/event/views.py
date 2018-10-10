from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from .models import Events, Rules, Registrations, Festmeta
from accounts.models import Staff, Students
from django.contrib.auth.models import AnonymousUser, User
from django.db.models import Count
from django.forms.models import model_to_dict
from django.contrib.auth import authenticate

def eventsindex(request):
    events = Festmeta.objects.all()
    if request.user.is_authenticated:
        user = request.user
        context = {'user':user,'events':events}
        return render(request,'event/index.html',context)
    else:
        context = {'events':events}
        return render(request,'event/index.html',context)

@login_required
def dashboard(request):
    context = {}
    user = User.objects.get(username=request.user.username)
    userobj = Students.objects.get(username=user.id)
    fests = Festmeta.objects.filter(username=user.username)
    regs = userobj.user_register.all()
    context = {'fests':fests,'user':user,'regs':regs}
    return render(request,'event/dashboard.html',context)

def events(request,pk):
    context = {}
    user_access = ''
    festobj = get_object_or_404(Festmeta,id=pk)
    events = Events.objects.filter(festname=festobj.pk)
    context = {'user_access':user_access,'events':events}
    return render(request,'event/events.html',context)

def displayevent(request,pk):
    context = {}
    regflag = False
    user = request.user
    event = get_object_or_404(Events,id=pk)
    if request.user.is_authenticated:
        student = Students.objects.get(username=user)
        regflag = Registrations.objects.filter(username=student,event=event).exists()
    rules = Rules.objects.filter(event=event)
    context = {'event':event,'rules':rules,'regflag':regflag,'user':user}
    return render(request,'event/displayevent.html',context)

@login_required
def addevent(request):
    user = request.user
    festpk = request.GET.get('festname')
    festobj = get_object_or_404(Festmeta,id=festpk,username=user.username)
    context = {'fest':festobj}
    if request.method == "POST":
        title = request.POST.get('title')
        category = request.POST.get('category')
        shortdesc = request.POST.get('shortdesc')
        briefdesc = request.POST.get('briefdesc')
        venue = request.POST.get('venue')
        date = request.POST.get('eventdate')
        dd,mm,yy = date.split('-')
        date = yy+'-'+mm+'-'+dd
        rules = request.POST.getlist('rule[]')
        registration_fee = request.POST.get('regfee')
        event = Events(festname=festobj,title=title,category=category,venue=venue,eventdate=date,short_desc=shortdesc,brief_desc=briefdesc,registration_fee=registration_fee)
        event.save()
        for rule in rules:
            ruleobj = Rules(event=event,rule=rule)
            ruleobj.save()
        return redirect('events',festpk)
    return render(request,'event/addevent.html',context)


@login_required
def registerevent(request):
    user = request.user
    pk = request.GET.get('id')
    student = Students.objects.get(username=user)
    event = Events.objects.get(id=pk)
    reg = Registrations(username=student,event=event,festmeta=event.festname,regfeestatus="No")
    reg.save()
    data = {'message':'Registration Successful'}
    return JsonResponse(data)


@login_required
def festmeta(request):
    if request.user.is_authenticated:
        user = request.user
        context = {'user':user}
        if request.method == "POST":
            festname  = request.POST.get('festname')
            start_date = request.POST.get('startdate')
            dd,mm,yy = start_date.split('-')
            start_date = yy+'-'+mm+'-'+dd
            end_date = request.POST.get('enddate')
            dd,mm,yy = end_date.split('-')
            end_date = yy+'-'+mm+'-'+dd
            description = request.POST.get('description')
            venue = request.POST.get('venue')
            college = request.POST.get('college')
            branch = request.POST.get('branch')
            address = request.POST.get('address')
            city = request.POST.get('city')
            district = request.POST.get('district')
            state = request.POST.get('state')
            pincode = request.POST.get('pincode')
            chiefguest1 = request.POST.get('chiefguest1')
            chiefguest2 = request.POST.get('chiefguest2')
            chiefguest3 = request.POST.get('chiefguest3')
            registrationfee = request.POST.get('registrationfee')
            accomodation = request.POST.get('accomodation')
            food = request.POST.get('food')
            spocname1 = request.POST.get('spocname1')
            spocname2 = request.POST.get('spocname2')
            spocmail1 = request.POST.get('spocmail1')
            spocmail2 = request.POST.get('spocmail2')
            spocphone1 = request.POST.get('spocphone1')
            spocphone2 = request.POST.get('spocphone2')
            festmail = request.POST.get('festmail')
            collegewebsite = request.POST.get('website')
            username = user.username
            f = Festmeta(festname=festname,start_date=start_date,end_date=end_date,description=description,venue=venue,college=college,college_address=address,city=city,district=district,state=state,pincode=pincode,chief_guest1=chiefguest1,chief_guest2=chiefguest2,chief_guest3=chiefguest3,registration_fee=registrationfee,accomodation=accomodation,food=food,spocname1=spocname1,spocname2=spocname2,spocmail1=spocmail1,spocmail2=spocmail2,spocphone1=spocphone1,spocphone2=spocphone2,festmail=festmail,collegewebsite=collegewebsite,username=username,branch=branch)
            f.save()
            fest = Festmeta.objects.get(festname=festname,username=username)
            return redirect('displayfest',fest.pk)
        return render(request,'event/festmeta.html',context)
    else:
        context = {'message':'You are not authorised to view this..!'}
        return render(request,'event/noaccess.html',context)

def displayfest(request,pk):
    user = request.user
    fest = get_object_or_404(Festmeta,id=pk)
    if request.user.is_authenticated:
        try:
            user = request.user
            user_access = Staff.objects.get(user=request.user)
            context = {'user_access':user_access,'user':user,'fest':fest}
            return render(request,'event/displayfest.html',context)
        except Staff.DoesNotExist:
            context = {'user_access':'','fest':fest}
            return render(request,'event/displayfest.html',context)
    else:
        context = {'user':user,'fest':fest}
        return render(request,'event/displayfest.html',context)

def home(request):
    user = request.user
    if request.user.is_authenticated:
        try:
            user = request.user
            user_access = Staff.objects.get(user=request.user)
            context = {'user_access':user_access,'user':user}
            return render(request,'event/home.html',context)
        except Staff.DoesNotExist:
            context = {'user_access':''}
            return render(request,'event/home.html',context)
    else:
        context = {'user':user}
        return render(request,'event/home.html',context)

def deletefest(request):
    pk = request.GET.get('pk')
    Festmeta.objects.get(id=pk).delete()
    data = {'message':'<div class="alert alert-success" role="alert">Event has been deleted</div>'}
    return JsonResponse(data)

def deleteevent(request):
    pk = request.GET.get('pk')
    Events.objects.get(id=pk).delete()
    data = {'message':'<div class="alert alert-success" role="alert">Sub-Event has been deleted</div>'}
    return JsonResponse(data)

def editfest(request,pk):
    fest = Festmeta.objects.get(id=pk)
    if request.method == "POST":
        fest.festname  = request.POST.get('festname')
        start_date = request.POST.get('startdate')
        dd,mm,yy = start_date.split('-')
        fest.start_date = yy+'-'+mm+'-'+dd
        end_date = request.POST.get('enddate')
        dd,mm,yy = end_date.split('-')
        fest.end_date = yy+'-'+mm+'-'+dd
        fest.description = request.POST.get('description')
        fest.venue = request.POST.get('venue')
        fest.college = request.POST.get('college')
        fest.branch = request.POST.get('branch')
        fest.college_address = request.POST.get('address')
        fest.city = request.POST.get('city')
        fest.district = request.POST.get('district')
        fest.state = request.POST.get('state')
        fest.pincode = request.POST.get('pincode')
        fest.chiefguest1 = request.POST.get('chiefguest1')
        fest.chiefguest2 = request.POST.get('chiefguest2')
        fest.chiefguest3 = request.POST.get('chiefguest3')
        fest.registration_fee = request.POST.get('registrationfee')
        fest.accomodation = request.POST.get('accomodation')
        fest.food = request.POST.get('food')
        fest.spocname1 = request.POST.get('spocname1')
        fest.spocname2 = request.POST.get('spocname2')
        fest.spocmail1 = request.POST.get('spocmail1')
        fest.spocmail2 = request.POST.get('spocmail2')
        fest.spocphone1 = request.POST.get('spocphone1')
        fest.spocphone2 = request.POST.get('spocphone2')
        fest.festmail = request.POST.get('festmail')
        fest.collegewebsite = request.POST.get('website')
        fest.save()
        return redirect('displayfest',pk)
    context = {'fest':fest}
    return render(request,'event/editfest.html',context)


def viewregistrations(request,pk):
    regs = Registrations.objects.filter(festmeta=pk)
    totalcount= len(regs)
    countbyevents = {}
    fest = Festmeta.objects.get(id=pk)
    events = fest.fest_event.all()
    for event in events:
        countbyevents[event.title] = len(event.event_register.all())
    context = {'regs':regs,'totalcount':totalcount,'countbyevents':countbyevents,'events':events,'festpk':pk}
    return render(request,'event/registrations.html',context)


def getregdetails(request):
    pk = request.GET.get('pk')
    festpk = request.GET.get('festpk')
    context = {}
    regs = ''
    if pk == '':
        regs = Registrations.objects.filter(festmeta=festpk).order_by('-id')
        context = {'regs':regs}
    else:
        event = Events.objects.get(id=pk)
        regs = Registrations.objects.filter(event=event,festmeta=festpk).order_by('id')
        context = {'regs':regs}
    return render(request,'event/regtable.html',context)

def changeregfee(request):
    pk = request.GET.get('pk')
    regobj = Registrations.objects.get(id=pk)
    if regobj.regfeestatus == "No":
        regobj.regfeestatus = "Yes"
    else:
        regobj.regfeestatus = "No"
    regobj.save()
    return JsonResponse(model_to_dict(regobj))


def profile(request):
    userobj = User.objects.get(username=request.user.username)
    profile = Students.objects.get(username=userobj)
    if request.method == "POST":
        profile.firstname = request.POST.get('firstname')
        profile.lastname = request.POST.get('lastname')
        dob = request.POST.get('dob')
        d,m,y = dob.split('-')
        dob = y+'-'+m+'-'+d
        profile.dob = dob
        profile.gender = request.POST.get('gender')
        profile.branch = request.POST.get('branch')
        profile.college = request.POST.get('college')
        profile.city = request.POST.get('city')
        profile.district = request.POST.get('district')
        profile.state = request.POST.get('state')
        profile.pincode = request.POST.get('pincode')
        profile.phone = request.POST.get('phone')
        profile.save()
        return redirect('profile')
    context = {'profile':profile,'user':userobj}
    return render(request,'event/profile.html',context)


def changepass(request):
    curpass = request.POST.get('curpass')
    newpass = request.POST.get('newpass')
    username = request.user.username
    message = ''
    obj = authenticate(username=username,password=curpass)
    if obj:
        user = User.objects.get(username=username)
        user.set_password(newpass)
        user.save()
        message = 'c'
    else:
        message = 'nc'
    data = {'message':message}
    return JsonResponse(data)


def userdisplay(request):
    pk = request.GET.get('pk')
    profile = Students.objects.get(id=pk)
    user = User.objects.get(id=profile.username_id)
    context = {'profile':profile,'user':user}
    return render(request,'event/profilemodal.html',context)
