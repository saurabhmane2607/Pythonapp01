import random
import string
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
import mysql.connector
from Firstapp01.models import urls




def index(request):
    print(request.POST)
    email=request.POST.get('email')
    email01=request.POST('email')
    return HttpResponse("Hello, world. You're at the polls index.")
def index1(request):
    email=request.GET.get('email')
    test= mysql.connector.connect(host="localhost",user="root",password="Saurabh@911",database="project")
    print(test)
    crs=test.cursor()
    crs.execute("Select * from country")
    for a in crs:
        print(a)
    return HttpResponse("Hello, index1")
def login(request):
    email=request.POST.get('email')
    password = request.POST.get('password')
    test= mysql.connector.connect(host="localhost",user="root",password="Saurabh@911",database="project")
    crs=test.cursor()
    query="select password from user where email = '"+email+"'"
    crs.execute(query)
    data=crs.fetchone()
    str= ""
    if data is None:
        str="You are not registered user"
    else:
        if data[0]==password:
            str= "You are valid user"
        else:
            str= "Your password is not correct"
    return HttpResponse(str)

def signup(request):
    email=""
    email = request.POST.get("email")
    password = request.POST.get("password")
    test = mysql.connector.connect(host="localhost", user="root", password="Saurabh@911", database="project")
    crs = test.cursor()
    query = "select * from ord where email = '" + email + "'"
    crs.execute(query)
    data = crs.fetchone()
    dict= {}
    if data is None:
        query= "insert into ord values ('" + email + "','" + password + "')"
        crs.execute(query)
        test.commit()
        dict['message']= 'registered'
        # return HttpResponse("registered")

    else:
        dict['message']='You are already registered user'
        # return HttpResponse("You are already registered user ")
    return JsonResponse(dict)

def getAllUser(request):
    test = mysql.connector.connect(host="localhost", user="root", password="Saurabh@911", database="project")
    crs = test.cursor()
    query = "select * from ord "
    crs.execute(query)
    data = crs.fetchall()
    dict = {}
    list=[]
    if data is None:
        dict['message']='No registered user'
    else:
        for l in data:
            d={}
            d['email']=l[0]
            d['password']=l[1]
            list.append(d)
        dict['data']=list
    return JsonResponse(dict)

def getStates(request):
    test = mysql.connector.connect(host="localhost", user="root", password="Saurabh@911", database="project")
    crs = test.cursor()
    query = "select * from state "
    crs.execute(query)
    data = crs.fetchall()
    dict = {}
    list = []
    if data is None:
        dict['message'] = 'State data not available'
    else:
        for l in data:
            d = {}
            d['state_id'] = l[0]
            d['state_name'] = l[1]
            list.append(d)
        dict['state'] = list
        dict['ttl']=24

    return JsonResponse(dict)

def getDistricts(request,id):
    test = mysql.connector.connect(host="localhost", user="root", password="Saurabh@911", database="project")
    stateId = request.GET.get("state_dis")
    crs = test.cursor()
    query = "select * from district where state_dis= "+id
    crs.execute(query)
    data = crs.fetchall()
    dict = {}
    list = []
    if data is None:
        dict['message'] = 'This state data not available'
    else:
        for l in data:
            d = {}
            d['district_id'] = l[0]
            d['district_name'] = l[1]
            list.append(d)
        dict['district'] = list
        dict['ttl']=24

    return JsonResponse(dict)
def shorturl(request):
    longurl= request.GET.get('longurl')
    customurl= request.GET.get('customurl')
    if customurl is None or customurl =="":
        while True:
            shorturl = generateRandomstring(6)
            data = urls.objects.filter(short_url=customurl)
            if len(data) == 0:
                url= urls(long_url=longurl, short_url=shorturl)
                url.save()
                break
    else:
        data = urls.objects.filter(short_url=customurl)
        if len(data) == 0:
            url1 = urls(long_url=longurl, short_url=customurl)
            url1.save()
        else:
            return HttpResponse ("Custom url already exist try something else")
    return HttpResponse("saved")

def generateRandomstring(size):
    letter= string.ascii_letters + string.digits
    shortUrl =''
    for i in range(size):
        shortUrl = shortUrl + ''.join(random.choice(letter))
    return shortUrl

def test5(request, ids):
    print(ids)
    return HttpResponse(ids)

def goToLongUrl(request, ids):
    data = urls.objects.filter(short_url=ids)
    print(data[0])
    return redirect(data[0].long_url)
    # if len(data) == 0:
    #     return HttpResponse("This shorturl not available")
    # # else:
    #     newdata= data[0]
    #     return redirect(newdata.long_url)