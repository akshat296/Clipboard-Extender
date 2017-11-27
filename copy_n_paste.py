import pyautogui
import sys
import subprocess
import os


myarr = os.environ["clip_var"]

i=0
s = '@!#!'
def copy(num_key):
    print(num_key)
    os.environ["clip_var"] = "check"
    flag=False
    pyautogui.hotkey('ctrl', 'insert')
    clip = subprocess.check_output('xclip -o', shell=True)
    pyautogui.alert('myarr %r'%myarr)
    clip = clip.decode("utf-8")
    for i in range(len(myarr)):
        if myarr[i] == clip:
            flag=True
            pyautogui.alert('Same Text at Num key %i'%i)
    if flag!=True: 
        myarr[int(num_key)]=clip
        pyautogui.alert('Text copied %s at Num key %i %r'%(clip,int(num_key),myarr))
        print(myarr)

def setClipboardData(data):
    p = subprocess.Popen(['xclip','-selection','clipboard'], stdin=subprocess.PIPE)
    p.stdin.write(data)
    p.stdin.close()
    retcode = p.wait()

def paste(num_key):
    print(myarr)
    if(myarr[int(num_key)]!=None):
        print(myarr[int(num_key)])
        setClipboardData(arr[int(num_key)].encode())
        pyautogui.PAUSE = 1
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.alert('Text pasted %s %r'%(clip,myarr))
    else:
        pyautogui.alert("Error None")           

if(sys.argv[1]=="copy"):
    copy(sys.argv[2])
if(sys.argv[1]=="paste"):
    paste(sys.argv[2])