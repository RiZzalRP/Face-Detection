import cv2
video=cv2.VideoCapture('/home/rizzal/Documents/git/Python/Opencv/mny1.mp4')

face_cascade = cv2.CascadeClassifier('/home/rizzal/Documents/git/Python/Face Detection/haarcascade_frontalface_default.xml')

while True:
    success,frame=video.read()
    if success == False:
        break
    rotate_frame = cv2.rotate(frame,cv2.ROTATE_90_COUNTERCLOCKWISE)

    grey = cv2.cvtColor(rotate_frame,cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(grey)

    for (x,y,w,h) in faces:
        rec = cv2.rectangle(
            rotate_frame,
            pt1=(x,y),
            pt2=(x+w,y+h),
            color=(10,255,10),
            thickness=2
            )
    cv2.imshow("Video",rotate_frame)
    if cv2.waitKey(3) & 0xFF==27:
        break

video.release()
cv2.destroyAllWindows()


# import cv2
# #  Load the pre-trained Haar Cascade classifier for face detection
# face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + '/home/rizzal/Documents/git/Python/Face Detection/haarcascade_frontalface_default.xml')

# # Open the video file
# cap = cv2.VideoCapture('/home/rizzal/Documents/git/Python/Opencv/mny1.mp4')

# while cap.isOpened():
#     # Read a frame from the video
#     ret, frame = cap.read()
#     if not ret:
#         break
    
#     # Convert the frame to grayscale
#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

#     # Detect faces
#     faces = face_cascade.detectMultiScale(gray)

#     # Draw rectangles around the detected faces
#     for (x, y, w, h) in faces:
#         cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

#     # Display the result
#     cv2.imshow('Face Detection', frame)

#     # Break the loop if 'q' is pressed
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# # Release resources
# cap.release()
# cv2.destroyAllWindows()