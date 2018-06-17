import praw
import urllib.request
import ctypes
import random
import os

def ChangeBack(lim , proirind):
        print('Getting Reddit Data...')
        reddit = praw.Reddit(client_id='m8WwEuPMiFFK2Q',
                             client_secret='N01fSGdUzH-m6RgHW3-u0GHUXSY',
                             user_agent='reddit_back',
                             username='ultramarinebot',
                             password='DingDong')

        walllist = []
        wallurl = []
        wallsubs = ['EarthPorn','SpacePorn']
        for wallsub in wallsubs:
                subreddit = reddit.subreddit(wallsub) 
                for submission in subreddit.hot(limit = lim):
                        if not submission.stickied:
                                wallurl.append(submission.url)
                                walllist.append(submission.url)
                                walllist.append(submission.title+'.'+submission.url.split('.')[-1])
            
               
        urltemp = ''
        chkind = -1
        for i in walllist:
                chkind+=1
                if i == wallurl[proirind]:
                        urltemp = walllist[chkind]
                        break


        
        SPI_SETDESKWALLPAPER = 20
        name = os.getcwd() + "\\temp."
        name += urltemp.split('.')[-1]
        SPIF_UPDATEINFILE = 1
        print('Downloading...', walllist[chkind+1])
        urllib.request.urlretrieve(urltemp,filename = 'temp.' + urltemp.split('.')[-1])
        print('Download Complete.\nSetting this as Wallpaper...')
        ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, name , SPIF_UPDATEINFILE)
        print('Wallpaper Set.')

        
        


if __name__ == "__main__":
        print('Welcome to Reddit-Background.')
        temp_limit = 100
        temp_proirind = random.randrange(1, temp_limit*2, 1)
        
        ChangeBack(temp_limit, temp_proirind)
        #input()


