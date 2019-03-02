#!/usr/bin/env python3

import praw
import urllib
import ctypes
import sys
import random
import os
import commands

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
        reddit = praw.Reddit(client_id=cl_id,
                             client_secret=cl_sc,
                             user_agent='reddit_back',
                             username=usrnm,
                             password=passwd)

        return reddit


def nameCorrector(name):
    #   Corrects file name in line with ubuntu file naming rules
    length = len(name)
    if length > 255:
        name = name[0:254]
    for i in range(0,length-1):
        if name[i] == '/':
            name[i] = '-'
    return name

#   Added so that wallsubs can be updated 
wallsubs = ['EarthPorn', 'SpacePorn']

def changeBack(lim , proirind, reddit):
        
        walllist = []
        wallups = []    
        
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
        name = nameCorrector(name)
        #	Downloading the file
        print('Downloading... ' + name)
        file_path = '/home/' + os.environ.get('USER') +'/Wallpapers/'
        urllib.urlretrieve(urltemp,filename = (file_path + name))
        print('Download Complete.\nSetting this as Wallpaper...')

        #	This part adds background support for ubuntu_gnome machines
        command = 'gsettings set org.gnome.desktop.background picture-uri file://' + file_path + '\"' + name+ '\"'
        status, output = commands.getstatusoutput(command)
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
                #Will add the option to add multis and subreddits
        
        reddit = setUp('ultramarinebot', 'DingDong', 'm8WwEuPMiFFK2Q', 'N01fSGdUzH-m6RgHW3-u0GHUXSY')
        changeBack(temp_limit, temp_proirind, reddit)


