import subprocess
def ReadFile():
    a=open("./gtools.txt")
    f=a.readlines()
    a.close()
    Split(f)
    
def Split(f):
    title=[]
    links=[]
    for i in range(len(f)):
        f[i]=f[i].split()
    for i in range(len(f)):
        if f[i][0][0]=='#':continue
        else:
            title.append(f[i][0])
            links.append(f[i][1])
    #print title,links
    Down(title,links)
    
def Down(title,links):
    for i in range(len(title)):
        print title[i]
        shells=subprocess.call("git clone "+links[i],shell=True)
        if shells==0:
            print title[i]+"Success\n"
        else:continue
        print "*********************************************"
if __name__ == '__main__':
    ReadFile()
