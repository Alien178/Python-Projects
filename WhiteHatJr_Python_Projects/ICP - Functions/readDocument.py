import time

def readDocument(filePath):
    file = open(filePath)
    read = file.read()
    words = read.split()
    print(len(words))
    
path = input("Please Enter the Path to the File.\n")
time.sleep(1)
print(path)
time.sleep(1)
readDocument(path)