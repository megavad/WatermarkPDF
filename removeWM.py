#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3
import re
import getopt, sys
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
root = tk.Tk()
root.withdraw()
file_path = filedialog.askopenfilename()
if file_path == '':
    exit(-1)
#print(file_path)
pos= 1
count  = 0
while pos > 0 :
    f = open(file_path, "rb+")
    byte = f.read()
    
    pos = byte.find(b'\x49\x6D\x61\x67\x65\x2F')
    #print (pos)
    
    if pos>0 :
        f.seek(pos)
        f.write(b'\xFF')
        count= count+1
        pos=1
    f.close()
messagebox.showinfo("Watermarks found ","Found "+ str(count)+" watermark(s)")

