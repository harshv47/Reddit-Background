import praw
import urllib.request
import ctypes
import sys
import random
import os
import subprocess

def printHelp():
	print('--------------------------------------------------------------------')
	print('Help Section:')
	print('Proper Usage: python script.py <arguments>')
	print('\t[-limit] [-help] [change_to] [random]')
	print(' -limit <int> :\tChanges the limit to the number upto which posts of each subreddit is checked. The default is 100.')
	print(' -help :\tDisplays this Section.')
	print(' change_to <int between 1 and limit (default = 100)> :\tChanges the backgroud to that rank if arranged on the basis of upvotes.')
	print(' random :\tChanges the background to a random image from the select pool upto limit.')

	print('\n\n\tIn case of conflicts the latter one will supercede the former.')
		
		
def setUp(usrnm, passwd, cl_id, cl_sc):
	print('Getting Reddit Data...')
	reddit = praw.Reddit(client_id=cl_id, client_secret=cl_sc, user_agent='reddit_back', username=usrnm, password=passwd)

	return reddit

def firstTimeLinux():
	file_path = '/home/' + os.environ.get('USER') +'/Pictures/'
	file = open(file_path + "_rb.dat", "w")
	file.write("Ran" + "\n")
	print('Write every input inside quotes')
	client_id = input('Please enter your Client ID:\t')
	client_secret = input('Please enter your Client Secret:\t')
	username = input('Please enter your Reddit Username:\t')
	password = input('Please enter your Reddit Password:\t')
	file.write(client_id + "\n")
	file.write(client_secret + "\n")
	file.write(username + "\n")
	file.write(password + "\n")
	file.close()

def swapper(str, ind, rep_ch):
	return (str[0:ind] + rep_ch + str[ind+1:len(str)])

def nameCorrectorLinux(name):
	#   Corrects file name in line with ubuntu file naming rules
	if len(name) > 255:
		name = name[0:254]
	for i in range(0,len(name)-1):
		if name[i] == '/':
			swapper(name, i, '-')
	return name

def nameCorrectorWindows(name):
	#   Corrects file name in line with Windows file naming rules
	if len(name) > 255:
		name = name[0:254]
	for i in range(0, len(name)-1):
		if name[i] in ['/', '\\']:
			swapper(name, i, '-')
		if name[i] == '<':
			swapper(name, i, '[')
		if name[i] == '>':
			swapper(name, i, ']')
		if name[i] in [':', '|', '?']:
			swapper(name, i, '_') 
		if name[i] == '\"':
			swapper(name, i, '\'')
		if name[i] == '*':
			swapper(name, i, 'x')
	return name

def changeBack(lim , proirind, reddit):
	
	walllist = []
	wallups = []    
	wallsubs = ['ultrahdwallpapers', 'WQHD_Wallpaper']
	reddit.read_only = True
	for wallsub in wallsubs:
		  subreddit = reddit.subreddit(wallsub)
		  for submission in subreddit.hot(limit = lim):          
					if not submission.stickied:
							upvotes = submission.ups
							wallups.append(upvotes)
							walllist.append(upvotes)
							walllist.append(submission.url)
							walllist.append(submission.title+'.'+submission.url.split('.')[-1])
		
		   
	proirind = -proirind
	urltemp = ''
	chkind = -1
	wallups.sort()
	for i in walllist:
			chkind+=1
			if i == wallups[proirind]:
					urltemp = walllist[chkind+1]
					break

	name = walllist[chkind+2]

	#   Checking for target machine to be a ubuntu desktop
	if os.environ.get("DESKTOP_SESSION") in ["ubuntu", "gnome", "unity"]:
		#   Correcting the file names
		name = nameCorrectorLinux(name)

		#   Downloading the file
		print('Downloading... ' + name)
		file_path = '/home/' + os.environ.get('USER') +'/Pictures/'
		
		#	Making the directory if it doesn't already exist
		if not os.path.exists(file_path):
			os.makedirs(file_path)

		urllib.request.urlretrieve(urltemp,filename = (file_path + name))
		print('Download Complete.\nSetting this as Wallpaper...')

		#   This part adds background support for ubuntu machines
		command = 'gsettings set org.gnome.desktop.background picture-uri file://' + file_path + '\"' + name+ '\"'
		status, output = subprocess.getstatusoutput(command)
		if status == 0:
			print('Wallpaper Set')
		else:
			print('Some error occured. Please Try Again; if the issue persists, pray')

	#   Checking for target machine to be a Windows desktop
	if sys.platform in ["win32", "cygwin"]:
		#   Correcting the file names
		name = nameCorrectorWindows(name)

		#   Downloading the file
		print('Downloading...', name)
		file_path = os.path.expanduser('~\\Pictures') +'\\Pictures\\'

		#	Making the directory if it doesn't already exist
		if not os.path.exists(file_path):
			os.makedirs(file_path)

		urllib.request.urlretrieve(urltemp,filename = (file_path + name))
		print('Download Complete.\nSetting this as Wallpaper...')

		#   This part adds back ground support for Windows machines
		SPI_SETDESKWALLPAPER = 20
		SPIF_UPDATEINFILE = 1
		command = file_path + name
		ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, command , SPIF_UPDATEINFILE)
		print('Wallpaper Set.')

	#   Checking for target machine to be Mate
	if os.environ.get("DESKTOP_SESSION") == "mate":
		#   Correcting the file names
		name = nameCorrectorLinux(name)

		#	Downloading th file
		print('Downloading... ' + name)
		file_path = '/home/' + os.environ.get('USER') +'/Pictures/'

		#	Making the directory if it doesn't already exist
		if not os.path.exists(file_path):
			os.makedirs(file_path)
		
		urllib.request.urlretrieve(urltemp,filename = (file_path + name))
		print('Download Complete.\nSetting this as Wallpaper...')

		#   This part adds background support for Mate machines
		file_path += '\"' + name+ '\"'
		command = 'mateconftool-2 -t string -s /desktop/mate/background/picture_filename ls' + file_path + ' | shuf -n1' 
		status, output = subprocess.getstatusoutput(command)
		if status == 0:
			print('Wallpaper Set')
		else:
			print('Some error occured. Please Try Again; if the issue persists, pray')

	#	Checking for the target machine to be Cinnamon
	if os.environ.get("DESKTOP_SESSION") == "cinnamon":
		#   Correcting the file names
		name = nameCorrectorLinux(name)

		#	Downloading th file
		print('Downloading... ' + name)
		file_path = '/home/' + os.environ.get('USER') +'/Pictures/'

		#	Making the directory if it doesn't already exist
		if not os.path.exists(file_path):
			os.makedirs(file_path)
		
		urllib.request.urlretrieve(urltemp,filename = (file_path + name))
		print('Download Complete.\nSetting this as Wallpaper...')

		#   This part adds background support for Cinnamon machines
		file_path += '\"' + name+ '\"'
		command = 'gsettings set org.cinnamon.desktop.background picture-uri  file://' + file_path
		status, output = subprocess.getstatusoutput(command)
		if status == 0:
			print('Wallpaper Set')
		else:
			print('Some error occured. Please Try Again; if the issue persists, pray')     
	
	


if __name__ == "__main__":
	print('Welcome to Reddit-Background. Use -help for list of Arguments.')
	temp_limit = 100
	temp_proirind = 1
	arg_counter = -1
	if len(sys.argv) < 2:
			print('Please provide proper argument(s). Use -help to see the list of Arguments. Defaulting to the highest upvoted post.')
			
	for argument in sys.argv:
			arg_counter += 1
			if argument == '-limit':
					temp_limit = int(sys.argv[arg_counter+1])
					
			if argument == '-help':
					printHelp()
					input()
					sys.exit()

			if argument == 'change_to':
					temp_proirind = int(sys.argv[arg_counter+1])
					
			if argument == 'random':
					temp_proirind = random.randrange(1, temp_limit, 1)
			#Will add the option to add multis and subreddtis
	
	file_path = '/home/' + os.environ.get('USER') +'/Pictures/'
	client_id = ''
	client_secret = ''
	username = ''
	password = ''
	if os.path.isfile(file_path + "_rb.dat"):
		#	If the file exists, meaning it has already been set up
		file = open(file_path + "_rb.dat", "r")
		lines = file.readlines()
		client_id = lines[1].strip()
		client_secret = lines[2].strip()
		username = lines[3].strip()
		password = lines[4].strip()
		file.close()

		#	Running the commands:
		reddit = setUp(username, password, client_id, client_secret)
		changeBack(temp_limit, temp_proirind, reddit)
	else:
		print("This is an Wallpaper Changer Application that uses Reddit!\n")
		print("To use this application you require a reddit account, you can create one at https://www.reddit.com/register")
		print("or if you already have one, log in at https://.reddit.com/login and add \"reddit_back\" as a script.")
		if os.environ.get("DESKTOP_SESSION") in ["ubuntu", "gnome", "unity", "mate", "cinnamon"]:
			firstTimeLinux()
		print('Reddit-Background is all Set up, run it again and enjoy!')

	
