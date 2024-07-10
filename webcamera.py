import cv2
web = cv2.VideoCapture(0)
face_casecade=cv2.CascadeClassifier('/home/rizzal/Documents/git/Python/Face Detection/haarcascade_frontalface_default.xml')

while True:
    success,frame = web.read()
    if success==False:
        break
    gry_web = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = face_casecade.detectMultiScale(gry_web)
    print(faces)

    for (x,y,w,h) in faces:
        img_rec = cv2.rectangle(
            frame,
            pt1=(x,y),
            pt2=(x+w,y+h),
            color=(10,255,20),
            thickness=2
            )
    cv2.imshow('Web Detection',frame)
    if cv2.waitKey(2) & 0xFF==27:
        break

web.release()
cv2.destroyAllWindows()
