import cv2
import glob
import time
from emailing import send_email
import os
from threading import Thread

video = cv2.VideoCapture(0)
time.sleep(1)

first_frame = None
status_list = []
count = 0


def clean_folder():
    images = glob.glob("images/*.png")
    for image in images:
        os.remove(image)

# email_sent = False
#
# def change_status():
#     email_sent = True

while True:
    status = 0
    check, frame = video.read()
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # Color grading - CAPITAL LETTER means ALGORITHMS
    gray_frame_gau = cv2.GaussianBlur(gray_frame, (21, 21), 0)  # Here (21, 21) is the amount of blur

    if first_frame is None:
        first_frame = gray_frame_gau #To assign the first frame if not done already
        continue

    delta_frame = cv2.absdiff(first_frame, gray_frame_gau)  # To show the difference between 2 frames

    thresh_frame = cv2.threshold(delta_frame, 50, 255, cv2.THRESH_BINARY)[1]  # Any pixel color code that is higher than
    # # 30 will be assigned color code of 255-white , getting index- 1 from the list
    dil_frame = cv2.dilate(thresh_frame, None, iterations=2)
    # cv2.imshow("My Video", dil_frame)

    contours, check = cv2.findContours(dil_frame, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        if cv2.contourArea(contour) < 13000:
            continue
        x, y, w, h = cv2.boundingRect(contour)
        rectangle = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)
        # Here (x,y),(x+w, y+h) are 2 diagonal corners of the same rectangle
        # (0, 255, 0) is for (B,G,R) so the color of rect will be GREEN
        # Last arg - 3 is the width of the border

        if rectangle.any():
            status = 1 #object found
            cv2.imwrite(f"images/{count}.png", frame)
            count = count + 1
            all_images = glob.glob("images/*.png")
            index = int(len(all_images) / 2)  # Because this has better chances to appear clearly
            image_with_object = all_images[index]

    status_list.append(status)
    status_list = status_list[-2:]

    if status_list[0] == 1 and status_list[1] == 0: #object has just exit from the frame
        email_thread = Thread(target=send_email, args=(image_with_object,))  # Thread definition
        email_thread.daemon = False # so even if the camera is closed the email is sent out

        email_thread.start()  # Thread call

    cv2.imshow("video", frame)
    # Contours means borders of where the motion is happening-for here
    key = cv2.waitKey(1)
    if key == ord("q"):
        break

video.release()
clean_folder()
