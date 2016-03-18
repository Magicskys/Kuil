import subprocess
a=open("./gtools.txt")
f=a.readlines()
a.close()
title=[]
links=[]
for i in range(len(f)):
    f[i]=f[i].split()
for i in range(len(f)):
    title.append(f[i][0])
    links.append(f[i][1])
print title,links
for i in range(len(title)):
    print title[i]
    shells=subprocess.call("git clone "+links[i],shell=True)
    if shells==0:
        print title[i]+" Success\n"
    else:continue
    print "*********************************************"
