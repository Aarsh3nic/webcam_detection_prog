import cv2
import numpy
import time

video = cv2.VideoCapture(0)
time.sleep(1)

first_frame = None

while True:

    check, frame = video.read()
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # Color grading - CAPITAL LETTER means ALGORITHMS
    gray_frame_gau = cv2.GaussianBlur(gray_frame, (21, 21), 0)  # Here (21, 21) is the amount of blur

    if first_frame is None:
        first_frame = gray_frame_gau

    delta_frame = cv2.absdiff(first_frame, gray_frame_gau)  # To show the difference between 2 frames

    thresh_frame = cv2.threshold(delta_frame, 30, 255, cv2.THRESH_BINARY)[1]  # Any pixel color code that is higher than
    # 30 will be assigned color code of 255-white , getting index- 1 from the list
    cv2.imshow("My Video", thresh_frame)

    key = cv2.waitKey(1)
    if key == ord("q"):
        break

video.release()
