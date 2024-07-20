import cv2 as cv
import yaml



def playback(camera):
    """
    Streams video to the monitor.
    """
    cap = cv.VideoCapture(camera)

    if not cap.isOpened():
        print("Cannot open camera")
        exit()

    # Capture frame-by-frame
    while True:
        ret, frame = cap.read()

        # If frame is read correctly ret is True
        if not ret:
            print("Can't read frame!")
            # Don't break -- the first frame may be empty if running this script at start-up.
            break

        # Operations on the frame come here
        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

        # Display the resulting frame
        cv.imshow("frame", gray)
        if cv.waitKey(1) == ord("q"):
            break
    
    # Elegantly shut down.
    cap.release()
    cv.destroyAllWindows()



if __name__ == "__main__":

    # Parse the config file.
    with open("config.yaml", "r") as yamlfile:
        config_data = yaml.load(yamlfile, Loader=yaml.FullLoader)

    camera = config_data["camera"]


    # Start the playback
    playback(camera)
