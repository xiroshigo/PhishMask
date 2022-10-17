import os

import colorama

import pyshorteners as sh

import pyshorteners

from colorama import init

from colorama import Fore, Back, Style



init(autoreset=True)

s = pyshorteners.Shortener()

s = sh.Shortener()





def cutlink():

	try:
		isgd = s.isgd.short(link__input)

		dagd = s.dagd.short(link__input)

		osdb = s.osdb.short(link__input)

		tinyurl = s.tinyurl.short(link__input)

		print("[" + Fore.GREEN + "TAYYOR" + Fore.WHITE + "] Havolalar muvaffaqiyatli yaratildi: \n")

		print(f'{isgd} \n{dagd} \n{osdb} \n{tinyurl}')

	except:

		print("[" + Fore.RED + "ОШИБКА" + Fore.WHITE + "] havola togri ekaniga ishonch hozil qiling va qaytadan urunih korjng")





def masklink():

	print("[" + Fore.GREEN + "TAYYOR" + Fore.WHITE + "] Havolalar muvaffaqiyatli yaratildi: \n")

	print("https://vk.com/away.php?photo435_33&to=" + link_input)

	print("https://www.youtube.com/redirect?q=" + link_input)

	print("https://www.google.com/url?q=" + link_input)

	print("https://m.ok.ru/dk?__dp=y&_prevCmd=altGroupMain&st.cln=off&st.cmd=outLinkWarning&st.rfn=" + link_input)

	print("https://l.facebook.com/l.php?u=" + link_input)

	print("https://raidforums.com/misc.php?action=safelinks&url=" + link_input)







banner = Fore.RED + """     _            _               _

  __| | __ _ _ __| | ___ __   ___| |_

 / _` |/ _` | '__| |/ / '_ \ / _ \ __|

| (_| | (_| | |  |   <| | | |  __/ |_

 \__,_|\__,_|_|  |_|\_\_| |_|\___|\__|""" + Fore.WHITE



maintext = f"""

{banner}





Script vazifasi phishing saytlarni maskirovka qilish

script @darknet_off1cial tomonidan tuzildi



[1] Maskirovka qilish ()

[2] Havolalarni qisqartirish

"""

os.system("termux-open-url https://t.me/darknet_off1cial")





while True:

	print(maintext)

	user_input = input('>>> ')



	if user_input == "1":

		print("[?] Maskirovka qimoqchi bogan havolangizni kiriting http/https. masalan: \nhttps://fishing-link.com \n")

		link_input = input(">>> ")

		masklink()



	elif user_input == '2':

		print("[?] http/https dan qisqartirilishi kerak bo'lgan havolani belgilang. Misol uchun: \nhttps://fishing-link.com \n")

		link__input = input(">>> ")

		cutlink()

	else:

		print("[" + Fore.RED + "XATOLIK" + Fore.WHITE + "] hato urunish ! qayadan sinab koring")
