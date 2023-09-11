import cv2
import matplotlib.pyplot as plt
import optoMDC

mre2 = optoMDC.connect() #Initialise mre2 object

#Set up settings for camera one - first axis of control
ch_0 = mre2.Mirror.Channel_0

ch_0.StaticInput.SetAsInput()                        
ch_0.InputConditioning.SetGain(1.0)                 
ch_0.SetControlMode(optoMDC.Units.XY)        
ch_0.LinearOutput.SetCurrentLimit(0.7)              

ch_0.Manager.CheckSignalFlow()          

#Set up settings for camera one - second axis of control
ch_1 = mre2.Mirror.Channel_1

ch_1.StaticInput.SetAsInput()                     
ch_1.InputConditioning.SetGain(1.0)                  
ch_1.SetControlMode(optoMDC.Units.XY)         
ch_1.LinearOutput.SetCurrentLimit(0.7)               

ch_1.Manager.CheckSignalFlow()                    


def map_value(value, old_min, old_max, new_min, new_max):
    mapped_value = (value - old_min) * ((new_max - new_min) / (old_max - old_min)) + new_min
    return mapped_value

#haarcascade classifer object
face_classifier = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

#Video capture object
video_capture = cv2.VideoCapture(0)  


plt.ion()  
fig, ax = plt.subplots()
x_data = []
y_data = []
line, = ax.plot(x_data, y_data, '-o', label='XY Coordinates')
ax.set_xlim(-1,1)  
ax.set_ylim(-1, 1)   
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_title('Live XY Plot')
ax.legend()

#Run facial detection 
def detect_bounding_box(vid):
    gray_image = cv2.cvtColor(vid, cv2.COLOR_BGR2GRAY)
    faces = face_classifier.detectMultiScale(gray_image,scaleFactor=1.1, minNeighbors=5, minSize=(40, 40))
    for (x, y, w, h) in faces:
        cv2.rectangle(vid, (x, y), (x + w, y + h), (0, 255, 0), 4)
        #print((x,y))
        print((map_value(x,0,int(video_capture.get(cv2.CAP_PROP_FRAME_WIDTH)),-1,1),map_value(x,0,int(video_capture.get(cv2.CAP_PROP_FRAME_HEIGHT)),-1,1)))
    return faces

#For loop for constant video capture
while True:
    ret, frame = video_capture.read()

    if not ret:
        break

    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_classifier.detectMultiScale(gray_frame, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))


    x_data.clear()
    y_data.clear()

    for (x, y, w, h) in faces:
        x_data.append(-1 + 2 * (x + w // 2) / frame.shape[1]) 
        y_data.append(-1 + 2 * (y + h // 2) / frame.shape[0])  


    line.set_xdata(x_data)
    si_1.setXY(x_data)
    line.set_ydata(y_data)
    si_0.setXY(y_data)
    plt.draw()
    plt.pause(0.01)  
    
    faces = detect_bounding_box(
        frame
    )  
    cv2.imshow(
        "Face Detection", frame
    )  
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
plt.ioff()  
plt.show()  
cv2.destroyAllWindows()
