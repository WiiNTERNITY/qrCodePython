from django.shortcuts import render
from django.contrib.auth.models import User , auth
from django.contrib.auth import authenticate, login
from django.http import JsonResponse ,HttpResponse
from django.views.decorators.csrf import csrf_exempt
from datetime import date,datetime,time
from nanapp.models import *
import json

import ipaddress
from django.utils.translation import ugettext_lazy as _



# Create your views here.

# Nan = ipaddress.ip_network('192.168.50.0/24')
# for x in Nan.hosts():
     
#     print(x)  



@csrf_exempt
def login(request):
    status = False
    message = ""
    data ={}
    if request.method == "POST":
        try:
            postdata = json.loads(request.body.decode('utf-8'))
            username =  postdata['username']
            password = postdata['password']
        except :
            username = request.POST.get('username',None)
            password = request.POST.get('password',None)
            
        user = authenticate(username=username, password=password)
        if user is not None:
            
            profile = Profile.objects.filter(user=user).values('contacts','user__username','genre','user__email','specialite','images',)[:1].get()
            
            data = {
                    'user':profile,
                    }
            return JsonResponse(data)

        else:
            
            return HttpResponse(status=401)

@csrf_exempt
def qrverif(request):
    status = False
    message = ""
    if request.method == "POST":
        try:
            postdata = json.loads(request.body.decode('utf-8'))
            username =  postdata['username']
            qrcode = postdata['qrcode']
            ip_adress = postdata['ip_adrrese']
        except :
            username = request.POST.get('username',None)
            ip_adress = request.POST.get('ip_adrrese',None)
            qrcode = request.POST.get('qrcode',None)
        try:
            user = User.objects.filter(username=username)[:1].get()
            if user is not None:
                if ipaddress.ip_address('{ip}'.format(ip=ip_adress)) in ipaddress.ip_network('192.168.50.0/24'):
                    try:
                        jours = date.today()
                        code = Qrcode.objects.filter(jours=jours)[:1].get()
                        if code.is_valid:
                            try:
                                profile = Profile.objects.filter(user=user)[:1].get()
                                presence = Presence.objects.filter(etudiant=profile,jour=jours)[:1].get()
                                if qrcode != code.titre_slug:
                                    status = False
                                    message = 'mauvais QR_CODE'
                                    return HttpResponse([] ,status=422)
                                elif presence.status == False:
                                    presence.status = True
                                    message = 'Success'
                                    status = True
                                    presence.save()
                                else:
                                    status = False
                                    message = 'Vous avez deja marquer votre Presence' 
                            except Exception as e:
                                message =str(e)
                            
                             
                        else:
                            return HttpResponse([] ,status=422)
                        
                    except :
                        pass
    
                else:
                    status = False
                    message = 'Vous devez etre a NaN avant de Scaner le QrCode' 
                    
                
        except Exception as e:
            
            message=str(e)
            status=False
            
    
 
    return JsonResponse({"status":status,"message":message},safe=True)