from bs4 import BeautifulSoup
import re
import socket
import urllib.request,urllib.parse, urllib.error
import json
import ssl

def file1(): 
    file = open('test.txt')
    fh = file.read()
    count = 0
    for line in fh:
        print(line)
        for word in line :
            if word is 't':
                count +=1
                continue
            else:
                continue
    print('The no. of times \'the\' was encountered:',count)
    file.close()

def assign2_2():
    file = open('test.txt')
    sum = 0
    s = list()
    lst = list()
    for line in file:
        lst = line.strip()
        x = re.findall('[0-9]+',lst)
        if len(x) == 0:
            continue
        elif len(x) >= 1:
            sumb = 0
            for c in x:
                sumb += int(c)
            s.append(sumb)
    for count in s:
        sum += count
    print(sum)
    
def htt():
    file = open('Tree_Pose_or_Vrksasana_.txt')
    s = list()
    lst = list()
    for line in file:
        lst = line.strip()
        x = re.findall('http+.*',lst)
        print(x)
    
def extract():
    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysock.connect(('data.pr4e.org',80))
    cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\n\n'.encode()
    mysock.send(cmd)

    while True:
        data = mysock.recv(512)
        if (len(data)<1):
            break
        print(data.decode())
    mysock.close()


def extract1():
    import socket

    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysock.connect(('data.pr4e.org', 80))
    cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()
    mysock.send(cmd)

    while True:
        data = mysock.recv(512)
        if len(data) < 1:
            break
        print(data.decode(),end='')
        print(data.URL())
    mysock.close()


def usingBS():
    #ignore SSL certificate errors
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    
    url = input('Enter - ')
    html = urllib.request.urlopen(url, context = ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('span')
    file = open('test1.txt','w')
    for tag in tags:
        tag.get('span',None)
        file.write(str(tag))
    file.close()
    file = open('test1.txt','r') 
    for line in file :
        lst = line.strip()
        num = re.findall('[0-9]+',lst)
    sumadd = 0 
    for numb in num:
        sumadd += int(numb)
    print('count ',len(num))
    print('sum ',sumadd)
    file.close()


def usingBS1():
    ctx = ssl.create_default_context()
    ctx.check_hostname= False
    ctx.verify_mode = ssl.CERT_NONE

    url = input('Enter - ')
    ch = 1
    tempurl = str()
    while ch <= 7:
        html = urllib.request.urlopen(url, context = ctx).read()
        x = BeautifulSoup(html, 'html.parser')
        tags = x('a')
        for tag in tags:
            print(tag.get('href',None))
            if tags.index(tag) == 17:
                url = tag.get('href',None)
                break
                '''
                    file = open('test2','w')
                    file.write(str(tag))
                    file.close()
                    file = open('test2.txt','r') 
                    for line in file :
                        lst = line.strip() 
                        tempurl= re.findall('http.+.html',lst)
                        '''
                   
        ch += 1

#http://py4e-data.dr-chuck.net/known_by_Fikret.html

def json1():
    serviceurl = 'http://py4e-data.dr.chuck.net?'

    while True:
        address = input('Enter : ')
        if len(address)< 1 :
            break

        url = serviceurl + urllib.parse.urlencode(
            {'address': address})
        print(url)
        uh = urllib.request.urlopen(url)
        data = uh.read().decode()
        print('retrieving',len(data),'characters')

        try:
            js = json.loads(data)
        except:
            js = None

        if not js or 'status' not in js or js['status'] != 'OK':
            print('Fail')
            print(data)
            continue

        print(json.dumps(js, indent=4))

htt()
        
