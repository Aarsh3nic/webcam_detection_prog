# Webcam Detection Program

This project consists of two Python files: `main.py` and `emailing.py`. The program is designed to detect any moving object that comes into the frame of a webcam. When a moving object is detected, an email notification is sent with an image attachment.

## `main.py`

This file contains the main code for webcam detection. It utilizes the OpenCV library to capture video from the webcam and perform motion detection. Here are the key features of the code:

- It captures video from the default webcam (index 0) using the `cv2.VideoCapture()` function.
- The first frame is saved as a reference for comparison with subsequent frames.
- The program calculates the difference between the first frame and the current frame to identify areas of motion.
- Thresholding and contour detection are applied to identify objects of significant motion.
- If an object is detected, the program saves the corresponding frame as an image in the `images/` directory.
- The program maintains a status history to determine when an object appears after being absent.
- When an object is detected after a period of absence, the `send_email()` function from `emailing.py` is invoked in a separate thread to send an email notification.

## `emailing.py`

This file contains the code for sending email notifications with image attachments. The email credentials are obtained from environment variables (`PASSforsecondarygmail`, `SENDER`, and `RECEIVER`). Here are the key features of the code:

- The `send_email()` function constructs an email message with a subject and content.
- It attaches the captured image to the email using the `EmailMessage` class from the `email.message` module.
- The script establishes a connection with the SMTP server, authenticates the sender's email address, and sends the email.

Note: The `PASSWORD` and email addresses (`SENDER` and `RECEIVER`) are retrieved from environment variables. Please ensure that you have set these environment variables with the appropriate values.

## Usage

1. Ensure that you have installed the required libraries, including OpenCV (`cv2`), smtplib, and imghdr.
2. Place both `main.py` and `emailing.py` in the same directory.
3. Set the required environment variables: `PASSforsecondarygmail`, `SENDER`, and `RECEIVER`.
4. Run `main.py` to start the webcam detection program.
5. When a moving object is detected, an email notification will be sent to the specified receiver email address.

Remember to grant appropriate permissions for accessing the webcam and sending emails.

## Author

This project was created by Aarsh Patel.
