from django.shortcuts import render,redirect
from django.http import JsonResponse
import json
from datetime import date,datetime,time
from  django.contrib.auth import  authenticate ,login ,logout
from django.contrib.auth.decorators import login_required
from django.core.validators import validate_email
from django.contrib.auth.models import User
from .import models
from django.utils.translation import ugettext_lazy as _
from .autotast.generateqrcode import generateqr
# Create your views here.

from datetime import date, timedelta
import calendar
# dt = date.today() - timedelta(7)
# dti = date.today() - timedelta(6)
# print(dti)

# print('Current Date :',date.today())
# print('5 days before Current Date :',dt)
# jan = models.Presence.objects.filter(jour__range=[dti, date.today()] ,status=True)
# feb = models.Presence.objects.filter(jour = dti ,status=True).count()
# print(jan,'------------------------------------',feb)
# label = []
# dataset = []
# for i in jan :
#     print(models.Presence.objects.filter(jour = i.jour ,status=True))
#     dataset.append(models.Presence.objects.filter(jour = i.jour ,status=True).count())
#     my_date = datetime.strptime(i.jour, "%Y-%m-%d")
#     print(my_date)
#     print('Day of Month:', my_date.day)
#     print('Day of Week (name): ', _(calendar.day_name[my_date.weekday()]))
#     label.append(_(calendar.day_name[my_date.weekday()]))
    
# print(dataset)
# print(label)

    
def login_page(request):
    return render(request,'dashbord/login.html')

def register(request):
    return render(request,'dashbord/register.html')

@login_required(login_url='login')

def index(request):
    nbr_student,nbr_presant,nbr_abs,dataset,label,nom ='','','',[],[],''
    try:
        ############ code for chartjs dinamise graphe  ##############
        
        dates7 = date.today() - timedelta(7)
        jour7 = models.Presence.objects.filter(jour = dates7 ,status=True).count()
        nom7= _(calendar.day_name[dates7.weekday()])  
            
        dates6= date.today() - timedelta(6)
        jour6 = models.Presence.objects.filter(jour = dates6 ,status=True).count()
        nom6= _(calendar.day_name[dates6.weekday()])                 
            
        dates5 = date.today() - timedelta(5)
        jour5 = models.Presence.objects.filter(jour = dates5 ,status=True).count()
        nom5= _(calendar.day_name[dates5.weekday()])
            
        dates4= date.today() - timedelta(4) 
        jour4 = models.Presence.objects.filter(jour = dates4 ,status=True).count()
        nom4= _(calendar.day_name[dates4.weekday()])
        
        dates3= date.today() - timedelta(3)
        jour3 = models.Presence.objects.filter(jour = date.today() - timedelta(3) ,status=True).count()
        nom3= _(calendar.day_name[dates3.weekday()])
            
        dates2 = date.today() - timedelta(2)
        jour2 = models.Presence.objects.filter(jour = dates2 ,status=True).count()
        nom2= _(calendar.day_name[dates2.weekday()])
        
        jour1 = models.Presence.objects.filter(jour = date.today() - timedelta(1) ,status=True).count()
        dates1= date.today() - timedelta(1)
        nom1 = _(calendar.day_name[dates1.weekday()])   

        jourj = models.Presence.objects.filter(jour = date.today() ,status=True).count()
        nomj= _(calendar.day_name[date.today().weekday()])

    
    except :
        pass


    try:
        isQr = models.Qrcode.objects.filter(jours=date.today(),status=True).exists() 
        qrDesactive = models.Qrcode.objects.filter(jours=date.today(),status=False).exists()
        todays = date.today()
        date_of_days = _(todays.strftime("%A"))
        groupe = models.Groupe.objects.filter(jour_passage__nom = date_of_days)
        for g in groupe:
            nom = g.nom
        nbr_student = models.Profile.objects.filter(groupe__nom = nom).count()
        nbr_presant=models.Presence.objects.filter(jour=date.today(),status=True).count()
        nbr_abs = models.Presence.objects.filter(jour=date.today(),status=False).count()
       

    except :
        pass
        

    if(isQr):
        try:
            
            myQr=models.Qrcode.objects.filter(jours=date.today(),status=True)[:1].get()
            list_presence = models.Presence.objects.filter(jour=date.today())

            data={
                'myQr':myQr,
                'isQr':True,
                'liste_presence':list_presence,
                'nbr_etudiant':nbr_student,
                'nbr_presant':nbr_presant,
                'nbr_abs':nbr_abs,
                'nom':nom,
                'nom1':nom1,
                'jour1':jour1,
                'nom2':nom2,
                'jour2':jour2,
                'nom3':nom3,
                'jour3':jour3,
                'nom4':nom4,
                'jour4':jour4,
                'nom5':nom5,
                'jour5':jour5,
                'nom6':nom6,
                'jour6':jour6,
                'nom7':nom7,
                'jour7':jour7,
                'nomj':nomj,
                'jourj':jourj,
                
                
            }
        except exception as e:
            pass

    elif qrDesactive:
        try:
            list_presence =models.Presence.objects.filter(jour=date.today())
            
            data={
            "isQr":False,
            'nbr_etudiant': nbr_student,
            'nbr_presant': nbr_presant,
            'liste_presence':list_presence,
            'nbr_abs': nbr_abs,
            'nom':nom,
            'nom1':nom1,
            'jour1':jour1,
            'nom2':nom2,
            'jour2':jour2,
            'nom3':nom3,
            'jour3':jour3,
            'nom4':nom4,
            'jour4':jour4,
            'nom5':nom5,
            'jour5':jour5,
            'nom6':nom6,
            'jour6':jour6,
            'nom7':nom7,
            'jour7':jour7,
            'nomj':nomj,
            'jourj':jourj,
            
            }
        except exception as e:
            pass


    else:
        data={
        "isQr":False,
        'nbr_etudiant': nbr_student,
        'nbr_presant': nbr_presant,
        'nbr_abs': nbr_abs,
        'nom':nom,
        'nom1':nom1,
        'jour1':jour1,
        'nom2':nom2,
        'jour2':jour2,
        'nom3':nom3,
        'jour3':jour3,
        'nom4':nom4,
        'jour4':jour4,
        'nom5':nom5,
        'jour5':jour5,
        'nom6':nom6,
        'jour6':jour6,
        'nom7':nom7,
        'jour7':jour7,
        'nomj':nomj,
        'jourj':jourj,
        }

    return render(request,'dashbord/index.html',data)


def scanner(request):

    try:
        isQr =models.Qrcode.objects.filter(jours=date.today(),status=True).exists()
        qrDesactive = models.Qrcode.objects.filter(jours=date.today(),status=False).exists()
    except exception as e:
        pass
    
    if(isQr):
        try:
            myQr=models.Qrcode.objects.filter(jours=date.today(),status=True)[:1].get()
            list_presence = models.Presence.objects.filter(jour=date.today())(0)
        except :
            pass
 
        data={
            'myQr':myQr,
            'isQr':True,
  
        }
    else:
        data={
        "isQr":False,
 
        }
    
    return render(request,'dashbord/qrCode_page.html',data)


def postLogin(request):
    if request.method == "POST":
        
        login_user = request.POST.get('login',False)
        password = request.POST.get('pass',False)
    
        user = authenticate(request,username=login_user,password=password)
        if user is not None and  user.user_profile.is_admin :
            login(request, user)
            return redirect('index')
        else:
           
            data={
                'error':True,
                'login':login,
                'pass':password
            }
        return render(request,'dashbord/login.html',data)
    
def postRegister(request):
    if request.method == "POST":
        
        try:
            login =request.POST.get('login',False)
            email =request.POST.get('email',False)
            password =request.POST.get('pass',False)
            repass = request.POST.get('repass',False)
        except exception as e:
            pass

        error=None
        print("################### registe post ###############")
        print(login,email,password)

    if(len(login) < 3):
        message='Login trop court '
        error =True
    if(password != repass):
        message ='Error password'
        error = True
    try:
        verifU = User.objects.filter(username=login)
    except :
        pass

    print(verifU)
    if(verifU):
        error =True
        message = "desole ce login existe dejat ;-("
   
    try:
        myU =User(username=login,email=email)
        myU.save()
        myU.password=password
        myU.set_password(myU.password)
        myU.save()
    except Exception as e :
        error =True
        message ="Error Username  "
    if(error):
        data={
            'error':True,
            'message':message,
            'login':login,
            'email':email,
            
        }
        return render(request,'pages/register.html',data)
    else:
        return redirect('index')

def addQrCode(request):
    try:
        post_data=json.loads(request.body.decode('utf-8'))
        jours =post_data['jours']
        hDebut=post_data['heurDebut']
        hFin=post_data['heurFin']
    except Exception as e:
        data={
            'success':False,
            'message':'Error de convertion des variables'
        }
        print("Error de recuperration des variables:",str(e))
    
    if hDebut > hFin:
        data={
            'success':False,
            'message':"Verifier l'heure de debut et l'heure de fin "
        }
    else:

        try:
            my_user =models.Qrcode.objects.filter(jours=date.today())[:1].get()
            qrExist=True
            
        except Exception as e:
            qrExist=False
            print("Exection Qr Existe ",str(e))
        
        if not qrExist:
            try: 
                qr = generateqr()
                new_qr_code = models.Qrcode(debut_heure_arrivee=hDebut,fin_heure_arrivee=hFin,created_by=request.user,titre_slug=qr)
                new_qr_code.save()
                # ceration de la liste de presance
                todays = date.today()
                date_of_days = _(todays.strftime("%A"))
                groupe = models.Groupe.objects.filter(jour_passage__nom__startswith = date_of_days)

                for g in groupe:
                    nom = g.nom
                all_user = models.Profile.objects.filter(groupe__nom = nom)

                for u in all_user:
                    now = datetime.now()
                    current_time = now.strftime("%H:%M:%S")
                    my_list = models.Presence(jour=date.today(),etudiant=u,qrcode=new_qr_code,heure_arrivee=current_time)
                    my_list.save()
                data ={
                    'success':True,
                    'message':'code qr genere avec succes'
                }
            except Exception as e:
                print("Error to adding Qr code ",str(e))
                data ={
                    'success':False,
                    'message':'Error dans creation du code Qr '
                }
        else:
            data ={
                'success':False,
                'message':'un Code Qr a déja été generer'
            }

    return JsonResponse(data,safe=True)

def unActiveQr(request):
    try:
        post_data=json.loads(request.body.decode('utf-8'))
        jours = date.today()
    except Exception as e:
        print("Error Recupperation veriable :",str(e))
        data={
            'success':False,
            'message':'Error Recupperation variable '
        }
    try:
        new_qr_code = models.Qrcode.objects.filter(jours=jours)[:1].get()
        new_qr_code.status=False
        new_qr_code.save()
        data={
            'success':True,
            'message':'Update ok '
        }
    except Exception as e:
        print("Error to find CodeQr ",str(e))
        data={
            'success':False,
            'message':'Error to find CodeQr '
        }
    return JsonResponse(data,safe=True)

def logout_page(request):
    logout(request)
    return redirect('login')
    