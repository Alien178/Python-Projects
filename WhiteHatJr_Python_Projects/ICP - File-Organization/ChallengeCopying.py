import os
import shutil

path = input("Please Enter the Path of the folder you want to copy!!\n")

destination = input("Please Enter the Path of the folder you want to copy the files to!!\n")

listOfFiles = os.listdir(path)

for file in listOfFiles:
    
    shutil.copy(path + "/" + file, destination)