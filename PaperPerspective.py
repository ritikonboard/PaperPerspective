import cv2 as cv
import numpy as np
import pyvirtualcam

# make sure you have the above libraries installed before runing the script. 
# You can install them by going in cmd prompt and running the folowing script: pip install opencv-python (it will install opencv and numpy), then, pip install pyvirtualcam

clicked_points = []
completed_clicks = False

# click on the four cornr points of the paper sheet/notbook/tab, that is to be transformed.
def mouse_callback(event, x, y, flags, param):
    global clicked_points, completed_clicks

    if event == cv.EVENT_LBUTTONDOWN:
        clicked_points.append((x, y))
        cv.circle(param, (x, y), 5, (0, 0, 255), -1)

        if len(clicked_points) == 4:
            completed_clicks = True

# make sure the aspect ratio of the frame and py virtual cam should be same.

def perspective_transform(frame):
    src_points = np.float32(clicked_points)
    dst_width = 1280
    dst_height = 720
    dst_points = np.float32([[0, 0], [dst_width, 0], [dst_width, dst_height], [0, dst_height]])
    matrix = cv.getPerspectiveTransform(src_points, dst_points)
    result = cv.warpPerspective(frame, matrix, (dst_width, dst_height))

    return result

def main():
    global clicked_points, completed_clicks
    
    # here in cv.videoCapture(x) - x = '0' is for your default laptop webcam, if theres any external camera then it will b denoted by x =1/2....
    cap = cv.VideoCapture(0)

    with pyvirtualcam.Camera(width=1280, height=720, fps=30) as cam:
        while True:
            ret, frame = cap.read()

            cv.putText(frame, "Click on the four corners of the A4 sheet.", (20, 30), cv.FONT_HERSHEY_TRIPLEX, 0.8, (0, 0, 255), 2)

            cv.imshow('Frame', frame)
            cv.setMouseCallback('Frame', mouse_callback, frame)

            if completed_clicks:
                corrected_frame = perspective_transform(frame)
                cv.imshow('Corrected Video Stream', corrected_frame)
                cam.send(corrected_frame)

            if cv.waitKey(1) & 0xFF == ord('q'):
                break

    cap.release()
    cv.destroyAllWindows()

if __name__ == "__main__":
    main()
