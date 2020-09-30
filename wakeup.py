import requests
import sys
if len(sys.argv) != 2:
	print('\n','Usage : python3 wakeup.py <ip to locate>')
	exit()

ip = str(sys.argv[1])
#defining the API's links for laer use
freegeoip_url = 'http://freegeoip.net/json/'
ip_api_url = "https://ipapi.co/{0}/json/"
geoip_nekudo_url = "http://geoip.nekudo.com/api/"
geoplugin_url = "http://www.geoplugin.net/json.gp?ip="
ip_api_com_url = "http://ip-api.com/json/"
#asking the API's for ip adresses locations
try :
	json_dict = requests.get((freegeoip_url + ip)).json()
	print('     freegeoip.net :')
	for prod in json_dict :
		print(prod,":",json_dict[str(prod)])
except :
	print("couldn't find the ip address in freegeoip database")
try :
	print('\n')
	json_dict = requests.get((ip_api_url.format(ip))).json()
	print('     ipapi.co :')
	for prod in json_dict :
		print(prod,":",json_dict[str(prod)])
except :
	print("couldn't find the ip address in ipapi database")
try :
	print('\n')
	json_dict = requests.get((geoip_nekudo_url + ip)).json()
	print('     geoip.nekudo.com :')
	for prod in json_dict :
		print(prod,":",json_dict[str(prod)])
except :
	print("couldn't find the ip address in nekudo-geoip database")
try :
	print('\n')
	json_dict = requests.get((geoplugin_url + ip)).json()
	print('     geoplugin.net :')
	for prod in json_dict :
		print(prod,":",json_dict[str(prod)])
except :
	print("couldn't find the ip address in geoplugin database")

try :
	print('\n')
	json_dict = requests.get((ip_api_com_url + ip)).json()
	print('     ip-api.com :')
	for prod in json_dict :
		print(prod,":",json_dict[str(prod)])
except :
	print("couldn't find the ip address in ip-api.com database")

