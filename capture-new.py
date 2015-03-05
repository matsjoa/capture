import cv2


videocap = cv2.VideoCapture("Filter-test.mp4")

success,image = videocap.read()

count = 0;
while success:
    success,image = videocap.read()
    cv2.imwrite("frame%d.jpg" % count, image)   # Save frame as JPEG file
    if cv2.waitKey(10) == 27:                   # Exit if Escape is hit
        break
    count += 1
