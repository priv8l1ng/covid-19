import requests, sys, re, time, os
from optparse import OptionParser

def banner(help=False, about=False):
        os.system("clear")
        print ("""
 \u001b[31m_   __                    _   _____\u001b[0m
\u001b[31m| | / /                   | | /  __ \ \u001b[0m
\u001b[31m| |/ /  __ ___      ____ _| | | /  \/ ___  _ __ ___  _ __   __ _\u001b[0m
\u001b[31m|    \ / _` \ \ /\ / / _` | | | |    / _ \| '__/ _ \| '_ \ / _` |\u001b[0m
| |\  \ (_| |\ V  V / (_| | | | \__/\ (_) | | | (_) | | | | (_| |
\_| \_/\__,_| \_/\_/ \__,_|_|  \____/\___/|_|  \___/|_| |_|\__,_|
   \u001b[31mAUTHOR: \u001b[0mMuhammad Lingga      \u001b[31mVERSION: \u001b[0mTESTER     \u001b[31mCOVID-19 \u001b[0mINFO\n\n""")
        if help == True:
                print("""
          \u001b[33mKNOWLEDGE ^_^
\u001b[32m[+] Command:
   	python/2/3 corona.py {option}
   	python/2/3 corona.py {country}

[+] Options:
   	-s, --save    = save result to file
   	-h, --help    = Help
   	-a, --about   = About
   	-c, --country = show all country list

[+] Country:
   	Detect All Country Bro\u001b[0m
""")
        if about == True:
                print ("""
\u001b[31mAuthor      : \u001b[0mMuhammad Lingga
\u001b[31mVersion    : \u001b[0mBeta Tester
\u001b[31mName       : \u001b[0mCorona Virus Info (Covid-19 Info)
\u001b[31mThanks     : \u001b[0mGods and all my friend
\u001b[31mFrom       : \u001b[0mapi.kawalcorona.com
\u001b[31mDescription: \u001b[0mshow information corona on all country
\u001b[31mLicense    : \u001b[0mMIT
""")

def get_information(country, save=False, path=None):
	print ("[!] Requests Get To URL", end="", flush=True)
	r = requests.get("https://api.kawalcorona.com").text
	print (" -> \u001b[32mSuccess\u001b[0m", end="", flush=True)
	print ("\n[!] Getting Information", end="", flush=True)
	get_country = re.findall('"Country_Region":"(.*?)"', r)
	data = '{"OBJECTID":(.*?),"Country_Region":"%s","Last_Update":(.*?),"Lat":(.*?),"Long_":(.*?),"Confirmed":(.*?),"Deaths":(.*?),"Recovered":(.*?),"Active":(.*?)}}'%(country)
	cari = re.search(data, r)
	print (" -> \u001b[32mSuccess\u001b[0m")
#	print (cari.group())
	last = str(cari.group(2))
	print ("\u001b[35m[+] Country: "+country)
	print ("\u001b[36m[+] Last Update: "+last)
	print ("\u001b[32m[+] Positif Corona: "+str(cari.group(5)), " Orang")
	print ("\u001b[31m[+] Meninggal : "+str(cari.group(6)), " Orang :(")
	print ("\u001b[33m[+] Sembuh Dari Corona: "+str(cari.group(7)), " Orang")
	print ("\u001b[32m[+] Active: "+str(cari.group(8))," Orang\u001b[0m")

def show_list():
	banner()
	try:
		o = open("list.txt", "r").read()
		for a in o.splitlines():
			print ("[+] "+str(a))
	except IOError:
		print ("[!] Requests Get To URL", end="", flush=True)
		r = requests.get("https://api.kawalcorona.com").text
		print (" -> \u001b[32mSuccess", end="", flush=True)
		print ("\n[!] Getting Country\n", end="", flush=True)
		country = re.findall('"Country_Region":"(.*?)"', r)
		for coun in country:
			print ("[+] "+str(coun), end="", flush=True)
			buka = open("list.txt", "a")
			buka.write(coun+"\n")
			buka.close()
			print (" -> \u001b[32mSuccess\n", end="", flush=True)

def main():
	save = None
	country = None
	parse = OptionParser(add_help_option=False, epilog="Corona Virus Information")
	parse.add_option("-s", "--save", help="Save Result", dest="save", action="store_false")
	parse.add_option("-h", "--help", help="Show All Commands", dest="help", action="store_true")
	parse.add_option("-a", "--about", help="About", dest="about", action="store_true")
	parse.add_option("-c", "--country", help="Show All Country", dest="country", action="store_true")
	opt, args = parse.parse_args()
	if opt.help == True:
		banner(help=True);sys.exit()
	elif opt.about == True:
		banner(about=True);sys.exit()
	elif opt.country == True:
		show_list()
	elif opt.save == True:
		try:
			save = args[0]
		except IndexError:
			banner(about=False);sys.exit()
	else:
		try:
			country = sys.argv[1]
		except IndexError:
			banner(help=True);sys.exit()
	if country:
		banner()
		try:
			o = open("list.txt", "r").read()
			for a in o.splitlines():
				if country.lower() in a.lower():
					if save:
						get_information(a, save=True, path=save)
					else:
						get_information(a)
					break
#				else:
#					print ("[#] Country '%s' Not Found, Please Use -c to show all country list"%(country));break
		except IOError:
			print ("[+] File List Country \u001b[31mNot Found\u001b[0m, please configure")
			sys.exit()
main()
