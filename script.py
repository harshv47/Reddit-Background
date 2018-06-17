import praw
import urllib.request
import ctypes
import sys
import random


def printHelp():
        print('--------------------------------------------------------------------')
        print('Help Section:')
        print('Proper Usage: python script.py <arguments>')
        print('\t[-limit] [-help] [change_to] [random]')
        print(' \t-limit <int> :\tChanges the limit to the number upto which posts of each subreddit is checked. The default is 100.\n
                \t-help :\tDisplays this Section.\n
                \tchange_to <int between 1 and limit (default = 100)> :\tChanges the backgroud to that rank if arranged on the basis of upvotes.\n
                \trandom :\tChanges the background to a random image from the select pool upto limit.\n
                
              ')

def ChangeBack(lim , proirind):
        print('Getting Reddit Data...')
        reddit = praw.Reddit(client_id='m8WwEuPMiFFK2Q',
                             client_secret='N01fSGdUzH-m6RgHW3-u0GHUXSY',
                             user_agent='reddit_back',
                             username='ultramarinebot',
                             password='DingDong')

        
        
        walllist = []
        wallups = []    
        wallsubs = ['EarthPorn', 'SpacePorn']
        
        for wallsub in wallsubs:
              subreddit = reddit.subreddit(walsub)
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
        name = os.getcwd() + "\\temp."
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
                #Will add the option to add multis and subreddits
        
        ChangeBack(temp_limit, temp_proirind)


