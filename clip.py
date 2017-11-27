import subprocess
import os
import subprocess
import pyautogui
import sys
i=0


def create_shortcut(name, command, binding):
    # defining keys & strings to be used
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
    cmd3 = 'gsettings set '+subkey1+new+" binding '"+binding+"'"

    for cmd in [cmd0, cmd1, cmd2, cmd3]:
        subprocess.call(["/bin/bash", "-c", cmd])


while i<10:
    create_shortcut("Copy Num %i"%i, "python3 /home/thinksysuser/Practise/clip/copy_n_paste.py '%s' '%i'"%('copy',i), "<Ctrl>%i"%i)
    create_shortcut("Paste Num %i"%i, "python3 /home/thinksysuser/Practise/clip/copy_n_paste.py '%s' '%i'"%('paste',i), "<Alt>%i"%i)
    print("loop %i"%i)
    i+=1

