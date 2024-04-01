import requests
import datetime
from requests.structures import CaseInsensitiveDict
import random

def readproxies(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file]

Intn = random.randint
Choice = random.choice
proxypath = "proxies.txt"

proxies = readproxies(proxypath)


def getuseragent():
	platform = Choice(['Macintosh', 'Windows', 'X11'])
	if platform == 'Macintosh':
		os  = Choice(['68K', 'PPC', 'Intel Mac OS X'])
	elif platform == 'Windows':
		os  = Choice(['Win3.11', 'WinNT3.51', 'WinNT4.0', 'Windows NT 5.0', 'Windows NT 5.1', 'Windows NT 5.2', 'Windows NT 6.0', 'Windows NT 6.1', 'Windows NT 6.2', 'Win 9x 4.90', 'WindowsCE', 'Windows XP', 'Windows 7', 'Windows 8', 'Windows NT 10.0; Win64; x64'])
	elif platform == 'X11':
		os  = Choice(['Linux i686', 'Linux x86_64'])
	browser = Choice(['chrome', 'firefox', 'ie'])
	if browser == 'chrome':
		webkit = str(Intn(500, 599))
		version = str(Intn(0, 99)) + '.0' + str(Intn(0, 9999)) + '.' + str(Intn(0, 999))
		return 'Mozilla/5.0 (' + os + ') AppleWebKit/' + webkit + '.0 (KHTML, like Gecko) Chrome/' + version + ' Safari/' + webkit
	elif browser == 'firefox':
		currentYear = datetime.date.today().year
		year = str(Intn(2020, currentYear))
		month = Intn(1, 12)
		if month < 10:
			month = '0' + str(month)
		else:
			month = str(month)
		day = Intn(1, 30)
		if day < 10:
			day = '0' + str(day)
		else:
			day = str(day)
		gecko = year + month + day
		version = str(Intn(1, 72)) + '.0'
		return 'Mozilla/5.0 (' + os + '; rv:' + version + ') Gecko/' + gecko + ' Firefox/' + version
	elif browser == 'ie':
		version = str(Intn(1, 99)) + '.0'
		engine = str(Intn(1, 99)) + '.0'
		option = Choice([True, False])
		if option == True:
			token = Choice(['.NET CLR', 'SV1', 'Tablet PC', 'Win64; IA64', 'Win64; x64', 'WOW64']) + '; '
		else:
			token = ''
		return 'Mozilla/5.0 (compatible; MSIE ' + version + '; ' + os + '; ' + token + 'Trident/' + engine + ')'
		
for current_proxy in proxies:
    url = "https://guns.lol/api/view/yourprofile"

    try:
        headers = CaseInsensitiveDict()
        headers["authority"] = "aknem.kyle"
        headers["accept"] = "*/*"
        headers["accept-language"] = "?0; Mobile"
        headers["cookie"] = "cf_clearance=PxQ43WBVlE73LEN3qiKC2gTauYIEhoSBh7cq.1lRoR8-1706625953-1-AfDAoZUap6+aQbhw/oJI0UGtVeGxnYfLaa3+jQMQM/Ll6nvJW4EViEuS/NXOogatEiFnNNY4Op+V5HgJwWJYBts=; _ga=GA1.1.787883208.1706625953; _ga_HVFV509737=GS1.1.1706625953.1.0.1706625953.0.0.0; _1__bProxy_v=defdb2f2cb4c2bacfea711befc12e794a5cea5742837e8fcc3369539c1da96ee"
        headers["user-agent"] = "getuseragent()"
        headers["verify_user"] = f"oQ0xoT_yourprofile"


    
        resp = requests.get(url, headers=headers, proxies={"https": current_proxy})
        print(f"Proxy: {current_proxy} | {resp.status_code} ")

    except requests.RequestException as e:
        print(f"Error using proxy {current_proxy}: {str(e)}")
