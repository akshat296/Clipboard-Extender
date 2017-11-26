# Enter script code
import tkinter as ttk
import os
import subprocess
import pyautogui
import sys
import subprocess

root = ttk.Tk()
root.title("My Clipboard")
arr = [None] * 11
i=0


def getClipboardData():
    p = subprocess.Popen(['xclip','-selection', 'clipboard', '-o'], stdout=subprocess.PIPE)
    retcode = p.wait()
    data = p.stdout.read()
    return data
def setClipboardData(data):
    p = subprocess.Popen(['xclip','-selection','clipboard'], stdin=subprocess.PIPE)
    p.stdin.write(data)
    p.stdin.close()
    retcode = p.wait()
def paste(event,clip2):
    if(arr[clip2]!=None):
        print(arr[clip2])
        setClipboardData(arr[clip2].encode())
        pyautogui.hotkey('ctrl', 'v')
    else:
        print("Error None")    

def copy(event,num_key):
    flag=False
    pyautogui.hotkey('ctrl', 'c')
    clip = subprocess.check_output('xclip -o', shell=True)
    clip = clip.decode("utf-8")
    for i in range(len(arr)):
        if arr[i] == clip:
            flag=True
            pyautogui.alert('Same Text at Num key %i'%i)
    if flag!=True: 
        arr[num_key]=clip
        print(arr)

def globalshortcut(name, command, shortcut_key):
    key = "org.gnome.settings-daemon.plugins.media-keys custom-keybindings"
    subkey1 = key.replace(" ", ".")[:-1]+":"
    item_s = "/"+key.replace(" ", "/").replace(".", "/")+"/"
    firstname = "custom"
    # get the current list of custom shortcuts
    get = lambda cmd: subprocess.check_output(["/bin/bash", "-c", cmd]).decode("utf-8")
    current = eval(get("gsettings get "+key))
    # make sure the additional keybinding mention is no duplicate
    n = 1
    while True:
        new = item_s+firstname+str(n)+"/"
        if new in current:
            n = n+1
        else:
            break
    # add the new keybinding to the list
    current.append(new)
    # create the shortcut, set the name, command and shortcut key
    cmd0 = 'gsettings set '+key+' "'+str(current)+'"'
    cmd1 = 'gsettings set '+subkey1+new+" name '"+name+"'"
    cmd2 = 'gsettings set '+subkey1+new+" command '"+command+"'"    
    cmd3 = 'gsettings set '+subkey1+new+" binding '"+shortcut_key+"'"

    for cmd in [cmd0, cmd1, cmd2, cmd3]:
        subprocess.call(["/bin/bash", "-c", cmd])
while i<10:
    root.bind("<Control-Key-%i>"%i,lambda event_copy, arg=i: copy(event_copy, arg))
    root.bind("<Alt-Key-%i>"%i,lambda event_paste, arg=i: paste(event_paste, arg))
    i+=1
globalshortcut("akshat","gedit","<Alt>8")         
root.mainloop()
