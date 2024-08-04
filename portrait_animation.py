import cv2
from datetime import datetime, timedelta
import yaml
import face_recognition
from picamera2 import Picamera2



# Parse the config file.
with open("config.yaml", "r") as yamlfile:
    config = yaml.load(yamlfile, Loader=yaml.FullLoader)


# Set up the camera
cv2.startWindowThread()
picam2 = Picamera2()
picam2.configure(picam2.create_preview_configuration(main={"format": "XRGB8888",
                                                            "size": (config["display_width"],
                                                                     config["display_height"])}))
picam2.start()

# Initialize this variable.
FACES = []


# Main event loop
while True:
    # Get a picture
    frame = picam2.capture_array()

    # Set to fullscreen
    cv2.namedWindow("window", cv2.WND_PROP_FULLSCREEN)
    cv2.setWindowProperty("window", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

    # Convert to gray, for face processing.
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Get the coordinates of the face.
    face_locations = face_recognition.face_locations(gray_frame)
    
    # If there is a face, begin streaming video while accumulating the frames in `FACES`
    if face_locations:
        FACES = []
        # # Draw bounding boxes around the faces.
        # # NOTE: only useful for debug
        # for top, right, bottom, left in face_locations:
        #     # Draw a box around the face
        #     cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
        #     if cv2.waitKey(20) & 0xFF == ord("q"):
        #         break

        # Record the start and end times to know how long to record for.    
        start = datetime.now()
        end = start + timedelta(seconds=config["recording_duration"])
        while datetime.now() < end:
            frame_inner = picam2.capture_array()
            FACES.append(frame_inner)

            cv2.imshow("window", frame_inner)

            # Boilerplate so video has time to display.
            if cv2.waitKey(20) & 0xFF == ord("q"):
                break

    # If no face is detected, but we have accumulates frames from previous faces, play them.
    elif FACES:
        for image in FACES:
            cv2.imshow("window", image)

            # Boilerplate so video has time to display.
            if cv2.waitKey(20) & 0xFF == ord("q"):
                break

    # If there is no face detected and no previously recorded faces, play back the video.
    else:
        cv2.imshow("window", frame)

    # Boilerplate so video has time to display.
    if cv2.waitKey(20) & 0xFF == ord("q"):
        break
