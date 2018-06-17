import praw
import urllib.request
import ctypes
import sys
import random

def printHelp():
        print('--------------------------------------------------------------------')
        print('Help Section:')
        print('Proper Usage:')

def ChangeBack(lim , proirind):
        print('Getting Reddit Data...')
        reddit = praw.Reddit(client_id='m8WwEuPMiFFK2Q',
                             client_secret='N01fSGdUzH-m6RgHW3-u0GHUXSY',
                             user_agent='reddit_back',
                             username='ultramarinebot',
                             password='DingDong')

        subreddit = reddit.subreddit('EarthPorn')
        
        walllist = []
        wallups = []    

        
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


        
        SPI_SETDESKWALLPAPER = 20
        name = "E:\\My\\Projects\\Reddit-Background\\temp."
        name += urltemp.split('.')[-1]
        print('Downloading...', walllist[chkind+2])
        urllib.request.urlretrieve(urltemp,filename = 'temp.' + urltemp.split('.')[-1])
        print('Download Complete.\nSetting this as Wallpaper...')
        ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, name , 0)
        print('Wallpaper Set.')

        
        


if __name__ == "__main__":
        print('Welcome to Reddit-Background. Use -help for list of Arguments.')
        temp_limit = 100
        temp_proirind = 1
        arg_counter = -1
        if len(sys.argv) < 2:
                print('Please provide proper argument(s). Use -help to see the list of Arguments.')
                
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
        
        ChangeBack(temp_limit, temp_proirind)


