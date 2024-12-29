import sys 
import os

path = os.getcwd()
 #print (path)
path= r'/DataFolder/Pandaspretty'
#print (path)
sys.path.append(os.path.abspath(path)) 
import Pandaspretty


path = os.getcwd() 
path+= r'/DataFolder'
sys.path.append(os.path.abspath(path)) 
import school_project