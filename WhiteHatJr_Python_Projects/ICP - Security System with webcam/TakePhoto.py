import cv2

def TakePhoto():
    videoCapture = cv2.VideoCapture(0)

    result = True

    while result:
        ret, frame = videoCapture.read()
        print(ret)
        cv2.imwrite("Picture.jpg", frame)
        result = False

    videoCapture.release()
    cv2.destroyAllWindows()

TakePhoto()