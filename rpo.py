#!/usr/bin/python3

import requests,sys,re
requests.packages.urllib3.disable_warnings()

print("""
  \033[92m\033[1m____  ____   ___    ____                                  
 |  _ \\|  _ \\ / _ \\  / ___|  ___ __ _ _ __  _ __   ___ _ __ 
 | |_) | |_) | | | | \\___ \\ / __/ _` | '_ \\| '_ \\ / _ \\ '__|
 |  _ <|  __/| |_| |  ___) | (_| (_| | | | | | | |  __/ |   
 |_| \\_\\_|    \\___/  |____/ \\___\\__,_|_| |_|_| |_|\\___|_| 

\033[0m\t\033[93m\033[1mRelative Path Overwrite (RPO - Scanner) - v1\033[0m
--------------------------------------------------------------------
 \033[92mCoded By \033[1m#Nittam\033[0m\033[92m\t\t\tCryptoGen Nepal Pvt. Ltd.
 https://nirmaldahal.com.np\t\thttps://cryptogennepal.com\033[0m
--------------------------------------------------------------------""")

def main():
	assert __file__ == sys.argv[0]
	try:
		url = sys.argv[1]
	except IndexError:
		print (" python3 rposcan.py <url>")
		sys.exit(2)

	headers = {
				'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36',
				'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
				'accept-language': 'en-US,en;q=0.9',
			}

	try:
		callTarget = requests.get(url, headers=headers, verify=False)
		href = re.findall(r"href=[\"|'](.*?\.css)",callTarget.text)

		print("\n \033[94mResult :\033[0m\n")

		for css in range(len(href)):
			if re.search(r"(https|http)", href[css]):
				print(" \033[93m[A]\033[0m\tAbsolute Path => "+href[css])
			elif re.search(r"^\/", href[css]):
				print(" \033[92m[R]\033[0m\tRelative Path => "+href[css])
			else:
				print(" \033[1m\033[91m[RPO]\033[0m\tRelative Path => \033[1m\033[91m"+href[css]+"\033[0m")
		pass
	except:
		print("\n Something Went Wrong!!!")

	print('''
\n--------------------------------------------------------------------
 \n\033[94mNote : \033[0m
 	\033[93m[A]\033[0m = Absolute Path (Not Vulnerable)
 	\033[92m[R]\033[0m = Relative Path (Not Vulnerable)
      \033[91m\033[1m[RPO]\033[0m = Possibly Vulnerable For Relative Path Overwrite (RPO) Attack\n
--------------------------------------------------------------------''')

if __name__ == '__main__':
	main()
