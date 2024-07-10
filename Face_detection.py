import cv2
img1 = cv2.imread('/home/rizzal/Documents/git/Python/Opencv/grp1.jpeg')

# Face Detection from image
face_casecade=cv2.CascadeClassifier('/home/rizzal/Documents/git/Python/Face Detection/haarcascade_frontalface_default.xml')

# for any detectio 1st preprcoseing is to convert the image in grey scale
gry_img = cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)


#Pass gry scale img to face cascade where its get the coordinate and its stored in array

faces = face_casecade.detectMultiScale(gry_img) 
print(faces)

# draw rectangle

for (x,y,w,h) in faces:
    img_rec = cv2.rectangle(
    img1,
    pt1=(x,y),
    pt2=(x+w,y+h),    # for geting 2nd point add x+width and y+height to get it
    color=(0,250,100),
    thickness=2
    )

cv2.imshow("Face Detection",img1)
cv2.waitKey()
cv2.destroyAllWindows()