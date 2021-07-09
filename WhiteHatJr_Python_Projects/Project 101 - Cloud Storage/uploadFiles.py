import os
import dropbox
from dropbox.files import WriteMode

class TransferData:
    def __init__(self, accessToken):
        self.accessToken = accessToken

    def uploadFiles(self, fileFrom, fileTo):
        dbx = dropbox.Dropbox(self.accessToken)

        for root, dirs, files in os.walk(fileFrom):

            for fileName in files:
                localPath = os.path.join(root, fileName)

                relativePath = os.path.realpath(localPath, fileFrom)
                dropboxPath = os.path.join(fileTo, relativePath)

                with open(localPath, "rb") as f:
                    dbx.files_upload(f.read(), dropboxPath, mode=WriteMode("overwrite"))

def main():
    accessToken = "pnK2-CLyR2kAAAAAAAAAAReDQtewbYyjg0_bjOrvhjOjz73e7gb6Yifz6xsAVFz_"
    transferData = TransferData(accessToken)

    fileFrom = str(input("Enter the Folder Path to Transfer:\n"))
    fileTo = input("Enter the Full Path to Upload to Dropbox:\n")

    transferData.uploadFiles(fileFrom, fileTo)
    print("The File has been Moved!!!")

main()