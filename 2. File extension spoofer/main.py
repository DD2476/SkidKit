import os, shutil, pystyle
def change(inFile, primaryExt, fakeExt):
    finalFile=os.path.basename(inFile).split('.')[0]+"‮"+fakeExt[::-1]+".."+primaryExt;shutil.copyfile(inFile, finalFile);return
def StartLogo():
    print(pystyle.Colorate.Horizontal(pystyle.Colors.blue_to_purple, pystyle.Center.XCenter("""
  ______      _                            __          
 |  ____|    | |                          / _|         
 | |__  __  _| |_   ___ _ __   ___   ___ | |_ ___ _ __ 
 |  __| \ \/ / __| / __| '_ \ / _ \ / _ \|  _/ _ \ '__|
 | |____ >  <| |_  \__ \ |_) | (_) | (_) | ||  __/ |   
 |______/_/\_\\\\__| |___/ .__/ \___/ \___/|_| \___|_|   
                       | |                             
                       |_|                             """)))
    print(f"Please insert the {pystyle.Colorate.Horizontal(pystyle.Colors.blue_to_purple, 'full path')} to your file: ")
    inFl = input()
    CheckFile(inFl)
    return
def CheckFile(inFl):
    if os.path.isfile(inFl):
        print(f"Please type your desired {pystyle.Colorate.Horizontal(pystyle.Colors.blue_to_purple, 'file extension')}: ")
        ext = input()
        if (ext.replace(" ", "") != ""):
            change(inFl, "pif", ext)
            print(pystyle.Colorate.Color(pystyle.Colors.green, "Success. Press any key to continue."))
            input()
            return
        else:
            print(pystyle.Colorate.Color(pystyle.Colors.red, "Please enter a valid extension."))
            print("")
            CheckFile(inFl)
            return
    else:
        os.system("cls" if os.name == 'nt' else "clear")
        print(pystyle.Colorate.Color(pystyle.Colors.red, "Please enter a valid file."))
        StartLogo()
        return
StartLogo()