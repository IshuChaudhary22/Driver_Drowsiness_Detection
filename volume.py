import cv2
print ("package imported")

cap=cv2.VideoCapture(0)

while True:
    succes, img =cap.read()
    cv2.imshow("img",img)
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break
