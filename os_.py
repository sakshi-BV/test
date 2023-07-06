
import os 
#present working directory
cwd = os.getcwd() 
print("Current working directory:", cwd)

#show list of all the files and directories
path = "/home/sakshi_sahu/Desktop/try"
dir_list = os.listdir(path)  
print("Files and directories in '", path) 
print(dir_list)