import cv2

img1 = cv2.imread('/home/rizzal/Documents/git/Python/Opencv/lk.jpeg')

eye_casecade = cv2.CascadeClassifier('/home/rizzal/Documents/git/Python/Face Detection/haarcascade_eye.xml')

gry_img = cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)

eyes= eye_casecade.detectMultiScale(gry_img)

for (x,y,w,h) in eyes:
    img_rec = cv2.rectangle(
    img1,
    pt1=(x,y),
    pt2=(x+w,y+h),    # for geting 2nd point add x+width and y+height to get it
    color=(0,250,100),
    thickness=2
    )

cv2.imshow("Eye Detect",img1)
cv2.waitKey()
cv2.destroyAllWindows()
    