from django.http import HttpResponse
from django.shortcuts import render, redirect
from subprocess import PIPE, Popen
import requests
import re, json
from django.conf import settings
from django.conf.urls.static import static
from django.views.decorators.csrf import csrf_exempt
import subprocess
from instabot import Bot
from auth import authenticate
import os

from datetime import datetime

album = None # You can also enter an album ID here

def login(request):
    return render(request, 'login/login.html')

def account(request):
  file = open('data.txt', 'r')
  data = eval(file.read())
  file.close()
  code = str(request.GET['code'])
  r = requests.post('https://leader-id.ru/api/oauth/access_token',data={'grant_type':'authorization_code','code':code,'client_id':'5262124a80a5f3a23e1ebf5e2a309d08','client_secret':'22a2efccce97e14f66e1416a8702ab47','redirect_uri':'http://85.143.216.153:8000/login'})
  json_p = eval(r.text)
  #print(json_p)
  r2 = requests.get('https://leader-id.ru/api/users/'+str(json_p['user_id'])+'?UserId='+str(json_p['user_id'])+'&access_token='+str(json_p['access_token']))
  json_p2 = json.loads(r2.text)
  print(json_p2)
  
  
  jp = {'insta':str(json_p2['Email'].split('@')[0]),
   'photo':str(json_p2['Photo']['Original']),
  'name':str(str(json_p2['FirstName'])+' ' +str(json_p2['LastName'])),
   'town':str(json_p2['Address']['City'])+','+str(json_p2['Address']['Country'])
   }
  jp['topic1'] = data['mas'][0]['topic']
  jp['des1'] = data['mas'][0]['des']
  jp['topic2'] = data['mas'][1]['topic']
  jp['des2'] = data['mas'][1]['des']
  jp['topic3'] = data['mas'][2]['topic']
  jp['des3'] = data['mas'][2]['des']
  jp['topic4'] = data['mas'][3]['topic']
  jp['des4'] = data['mas'][3]['des']
  #print({'photo':str(json_p2['Photo']['Original']), 'name':str(json_p2['FirstName'])})
  return render(request, 'account/account.html', jp)

def account2(request):
  print(request.GET)
  return HttpResponse("HI")

def index2(request):
  file = open('data.txt', 'r')
  data = eval(file.read())
  file.close()
  file = open('data2.txt', 'r')
  data2 = eval(file.read())
  file.close()
  jp = {'image1':''}
  print(data2[0])
  jp['image1'] = str(data2[-1])
  jp['image2'] = str(data2[-2])
  jp['image3'] = str(data2[-3])
  jp['image4'] = str(data2[-4])
  jp['topic1'] = data['mas'][0]['topic']
  jp['des1'] = data['mas'][0]['des']
  jp['topic2'] = data['mas'][1]['topic']
  jp['des2'] = data['mas'][1]['des']
  jp['topic3'] = data['mas'][2]['topic']
  jp['des3'] = data['mas'][2]['des']
  jp['topic4'] = data['mas'][3]['topic']
  jp['des4'] = data['mas'][3]['des']
  f = requests.post('http://85.143.216.153:8000/upload')
  return render(request, 'home.html', jp)

def form(request):
  return render(request, 'form/form.html')

@csrf_exempt
def upload(request):
  medias = bot.get_total_hashtag_medias('dobronews2019', amount=1, filtration=False)
  print(medias)
  bot.download_photos(medias, save_description=True)
  imgs = {}
  path = "./photos"
  valid_images = [".jpg"]
  cnt = 0
  for f in os.listdir(path):
    ext = os.path.splitext(f)[1]
    if ext.lower() not in valid_images:
      continue
    image = upload_kitten(client,path+'/'+f)
    imgs[cnt] = image['link']
  cnt += 1
  return HttpResponse(str(imgs))

@csrf_exempt
def update(request):
  file = open('data.txt', 'r')
  data = eval(file.read())
  file.close()
  if data['id'] == 4:
    data['id'] = 0
  data['mas'][data['id']]['topic'] = request.POST['topic']
  data['mas'][data['id']]['des'] = request.POST['descr']
  data['id'] += 1
  file = open('data.txt', 'w')
  file.write(str(data))
  file.close()
  return HttpResponse("HI")
  
