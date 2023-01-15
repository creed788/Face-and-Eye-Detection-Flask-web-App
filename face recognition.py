from flask import Flask, render_template, Response, url_for
import cv2
app = Flask(__name__)
camera = cv2.VideoCapture(0)

def gen_frame():
  while True:
    success, frame  = camera.read()
    # body_cascade = cv2.CascadeClassifier('haarcascades\haarcascade_upperbody.xml')
    detector = cv2.CascadeClassifier('haarcascades\haarcascade_frontalface_default.xml')
    eye_cascade = cv2.CascadeClassifier('haarcascades\haarcascade_eye_tree_eyeglasses.xml')
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = detector.detectMultiScale(gray, 1.1 ,3)
    #Draw Rectangle around each Faces.
    for (x,y,w,h) in faces:
      cv2.rectangle(frame, (x,y), (x+w, y+h), (255, 0, 0), 2)
      roi_gray = gray[y:y+h, x:x+w]
      roi_color = frame[y:y+h, x:x+w]
      eyes = eye_cascade.detectMultiScale(roi_gray, 1.1, 3)
      for (ex, ey, ew, eh) in eyes:
         cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0,255,0), 2)

    ret, buffer = cv2.imencode('.jpg', frame)
    frame = buffer.tobytes()
    yield(b'--frame\r\n'
                b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


@app.route('/')
def index():
  return render_template('index.html')

@app.route('/video_feed')
def video_feed():
  return Response(gen_frame(), mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/stop')
def stop():
  cv2.destroyAllWindows()

if __name__ == '__main__':
  app.run(debug = True)        



