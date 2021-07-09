import dropbox

class TransferData:
    def __init__(self, accessToken):
        self.accessToken = accessToken

    def uploadFile(self, fileFrom, fileTo):
        dbx = dropbox.Dropbox(self.accessToken)

        with open(fileFrom, "rb") as f:
            dbx.files_upload(f.read(), fileTo)

def main():
    accessToken = "jT1_Fij8KjgAAAAAAAAAARdn6pgFqggCozTrJLMyGBlOPcdGk9alA9zB7CK9sIsQ"
    transferData =  TransferData(accessToken)



    fileFrom = input("The Path to the File, you want to Upload to Dropbox\n")
    fileName = input("The Name of the File that is going to be Uploaded to Dropbox\n")
    fileTo = "/test_dropbox/" + fileName

    transferData.uploadFile(fileFrom, fileTo)

if __name__ == '__main__':
    main()