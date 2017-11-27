import pyautogui
import sys
import subprocess
import os

i=0
myarr = [0,1,2,3,4,5,6,7,8,9,10,11]
def fileread(num_key):
    try:
        f = open("clipped_at_NumKey_%i.txt"%num_key,'r')
        contents = f.read()
        return contents
    except IOError:
        return ''
def filewrite(num_key,txt):
    f = open("clipped_at_NumKey_%i.txt"%num_key,"w+")
    f.write(txt)
    pyautogui.alert('Text copied "%s" at Num-key-%i'%(txt,num_key))
    f.close()
    

def copy(num_key):
    print(num_key)
    flag=False
    pyautogui.hotkey('ctrl', 'insert')
    clip = subprocess.check_output('xclip -o', shell=True)
    clip = clip.decode("utf-8")
    for i in range(len(myarr)):
        f = fileread(i)
        if f == clip:
            flag = True
            pyautogui.alert('Same Text at Num-key-%i "%s"'%(i,f))
    if flag!=True: 
        filewrite(int(num_key),clip)
        print(clip)

def setClipboardData(data):
    p = subprocess.Popen(['xclip','-selection','clipboard'], stdin=subprocess.PIPE)
    p.stdin.write(data)
    p.stdin.close()
    retcode = p.wait()

def paste(num_key):
    print(num_key)
    f = fileread(int(num_key))
    if(f!=''):
        print(f)
        setClipboardData(f.encode())
        pyautogui.PAUSE = 1
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.alert('Text Pasted as "%s"'%f)
    else:
        pyautogui.alert("Nothing at Num-key-%i Error"%num_key)           

if(sys.argv[1]=="copy"):
    copy(sys.argv[2])
if(sys.argv[1]=="paste"):
    paste(sys.argv[2])