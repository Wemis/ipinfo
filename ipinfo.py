import requests
import time 
import os

def banner():
	return os.system("figlet IP info"), os.system("echo 'Tik Tok: @da.shaa_so2'|lolcat")

def ip():
	os.system("clear")
	banner()
	print("Введите IP адрес:")
	ip = input(">>> ")
	if ip == "":
		print("\n Вы ничего не ввели!")
	else:
		try:
			respone=requests.get('https://ipinfo.io/' + ip + '/json')
		except:
			print("ОшибОчка, ну блять")
			print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
			menu()
		p=respone.json()
		try:
			try:
				print("Айпишник бляди : " + p['ip'])
			except:
				pass
			try:
				print("Где оно находится : " + p['country'])
			except:
				pass
			try:
				print("Регион : " + p['region'])
			except:
				pass
			try:
				print("Городок : " + p['city'])
			except:
				pass
			try:
				print("Устройство : " + p['hostname'])
			except:
				pass
			try:
				print("Координаты : " + p['loc'])
			except:
				pass
			try: 
				print("Провайдер : " + p['org'])
			except:
				pass
			try:
				print("Часовой пояс : " + p['timezone'])
			except:
				pass
			try:
				print("Почтовой индекс : " + p['postal'])
			except:
				pass
		except:
			print("ОшибОчка, ну блять")
			print(">>>>>>>>>>>>>>>>>>>>>>>>>>>")
			menu()


def menu():
	banner()
	print("[1] IP info")
	print("[2] Exit")
	a = int(input(">>> "))
	if a == 1:
		ip()
	if a == 2:
		os.system("exit")

if __name__ == "__main__":
	menu()