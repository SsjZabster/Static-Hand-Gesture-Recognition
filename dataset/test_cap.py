import time
import numpy as np
import cv2

cap = cv2.VideoCapture(0)
count = 0
while(True):
    s_time= time.time()
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
    cv2.imshow('frame',gray)
    cv2.imwrite("frame%d.jpg" % count, frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    count += 1
    time.sleep(0.2 + (time.time() - s_time))

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()


