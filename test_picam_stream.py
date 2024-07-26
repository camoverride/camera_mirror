import cv2
import face_recognition
from picamera2 import Picamera2



# Set up the camera
cv2.startWindowThread()
picam2 = Picamera2()
picam2.configure(picam2.create_preview_configuration(main={"format": "XRGB8888",
                                                            "size": (1080, 1920)}))
picam2.start()

while True:
    frame = picam2.capture_array()

    # Set to fullscreen
    cv2.namedWindow("window", cv2.WND_PROP_FULLSCREEN)
    cv2.setWindowProperty("window", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    face_locations = face_recognition.face_locations(gray_frame)
    
    if face_locations:
        print(face_locations)
        # Draw bounding boxes around the faces
        for top, right, bottom, left in face_locations:
            # Draw a box around the face
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
    
    cv2.imshow("window", frame)


    if cv2.waitKey(20) & 0xFF == ord("q"):
        break
