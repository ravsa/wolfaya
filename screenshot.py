import os,subprocess
path=subprocess.Popen('which wkhtmltoimage',shell=True,stdout=subprocess.PIPE).communicate()[0]
def screen_shot(url,dir,filename):
    global path
    try:
        cmd=path[:-1]+' '+url+' '+dir+filename+'.jpg'
        a=subprocess.Popen(cmd,shell=True,stderr=subprocess.PIPE).communicate()[0]
    except Exception,e:
        print e

