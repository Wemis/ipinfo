import os
import time
try:
	import requests
	from colorama import Fore, Style, init
except:
	print("[-] All modules not installed. Run pip install -r requirements.txt for installing.")
        os.system("pip install -r requirements.txt")


def error():
    print(Fore.RED + "[-] Error")
    Style.RESET_ALL
    time.sleep(1)

def banner():
	return os.system("figlet IP info"), os.system("echo 'Tik Tok: @da.shaa_so2'|lolcat"), os.system("echo Instagram: wemis.github|lolcat")

def ip():
	os.system("clear")
	banner()
	print("")
	print("")
	print(Fore.MAGENTA + "╔══Input IP adress:")
	Style.RESET_ALL
	ip = input(Fore.MAGENTA + "╚════> ")
	Style.RESET_ALL
	if ip == "":
		print("\n you did not enter anything!")
	else:
		try:
			respone=requests.get('https://ipinfo.io/' + ip + '/json')
		except:
			print("Error 1000-7")
			print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
			menu()
		p=respone.json()
		try:
			try:
				print("IP Adress         : " + p['ip'])
			except:
				pass
			try:
				print("Country           : " + p['country'])
			except:
				pass
			try:
				print("Region            : " + p['region'])
			except:
				pass
			try:
				print("City              : " + p['city'])
			except:
				pass
			try:
				print("Hostname          : " + p['hostname'])
			except:
				pass
			try:
				print("Location          : " + p['loc'])
			except:
				pass
			try: 
				print("Provider          : " + p['org'])
			except:
				pass
			try:
				print("Timezone          : " + p['timezone'])
			except:
				pass
			try:
				print("Postal            : " + p['postal'])
				print(p)
			except:
				pass
		except:
			error()
			print(">>>>>>>>>>>>>>>>>>>>>>>>>>>")
			os.system("clear")
			menu()


def menu():
	banner()
	print("[1] IP info")
	print("[2] Github page")
	print("[3] Instagram page")
	print("[4] Exit")
	a = int(input(">>> "))
	if a == 1:
		ip()
	if a == 2:
		os.system("termux-open https://github.com/Wemis")
	if a == 3:
	    os.system("termux-open https://instagram.com/wemis.github?igshid=YmMyMTA2M2Y=")
	if a == 4:
	    os.system("exit")

if __name__ == "__main__":
	menu()
