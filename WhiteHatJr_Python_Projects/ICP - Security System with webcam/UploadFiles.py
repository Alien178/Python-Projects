import random
import dropbox
import time
import cv2

starttime = time.time()

def TakeSnapshot():
    number = random.randint(0, 100)

    cam = cv2.VideoCapture(0)
    result = True

    while result:
        ret, frame = cam.read()
        imageName = "img" + str(number) + ".png"

        cv2.imwrite(imageName, frame)

        starttime = time.time()

        result = False

    return imageName
    print("Snapshot Taken")

    cam.release()
    cv2.destroyAllWindows()

def UploadFile(imageName):
    accessToken = "jT1_Fij8KjgAAAAAAAAAARdn6pgFqggCozTrJLMyGBlOPcdGk9alA9zB7CK9sIsQ"

    fileFrom = imageName
    fileTo = "/images/" + imageName

    dbx = dbx = dropbox.Dropbox(accessToken)

    with open(fileFrom, "rb") as f:
            dbx.files_upload(f.read(), fileTo, mode=dropbox.files.WriteMode.overwrite)
            print("File Uploaded")

def main():
    while True:
        if (time.time() - starttime >= 10):
            name = TakeSnapshot()
            UploadFile(name)

if __name__ == '__main__':
    main()

