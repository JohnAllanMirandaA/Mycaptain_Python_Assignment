import os
filename = input("Input the Filename: ")  
name, ext = os.path.splitext(filename)   
ext_with_dot = ext[1:]
print ("The extension of the file is : " + ext)
