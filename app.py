import cv2
cap = cv2.VideoCapture(0)

#DIV, XVID, MJPG, X264, WMV1, WMV2
fourcc = cv2.VideoWriter_fourcc(*"XVID")
output = cv2.VideoWriter("output1.avi", fourcc, 20.0,(640,480),0)
#CONTAINS FOUR PARAMETER NAMED(name, CODEC, FPS, resolution)
print(cap)

while cap.isOpened():
  ret, frame = cap.read()
  if ret == True:
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.flip(gray, 0)
    cv2.imshow('gray', gray)
    cv2.imshow('original', frame)
    output.write(gray)
    if cv2.waitKey(1)== ord('g'):
      break
cap.release()  
output.release()
cv2.destroyAllWindows()