import pyzed.sl as sl
import cv2
import numpy as np

zed = sl.Camera() #create camera object

#set config parameters
init_params = sl.InitParameters()
init_params.camera_resolution = sl.RESOLUTION.HD1080
init_params.camera_fps = 30
init_params.sdk_verbose = True
init_params.depth_mode = sl.DEPTH_MODE.PERFORMANCE

#open camera
err = zed.open(init_params)
if (err != sl.ERROR_CODE.SUCCESS):
    exit(-1)

image = sl.Mat()
point_cloud = sl.Mat()

for i in range(150):
    # Grab an image
    if (zed.grab() == sl.ERROR_CODE.SUCCESS):
        zed.retrieve_image(image, sl.VIEW.LEFT) 
        zed.retrieve_measure(point_cloud,sl.MEASURE.XYZRGBA) #retrieve coloured point cloud
        
        gray_frame = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        gray_frame[gray_frame<240]=0
        
        circles = cv2.HoughCircles(gray_frame, cv2.HOUGH_GRADIENT, dp=1, minDist=50, param1=30, param2=15, minRadius=10, maxRadius=100)
        if circles is not None:
            circles = np.uint16(np.around(circles))
        
            for circle in circles[0, :]: #draw circles around the models circles
                cv2.circle(gray_frame, (circle[0], circle[1]), circle[2], (0, 255, 0), 2)
                cv2.circle(gray_frame, (circle[0], circle[1]), 2, (0, 0, 255), 3)

                print(f"Circle Center: X = {circle[0]}, Y = {circle[1]}")
        cv2.imshow("Gray Image",gray_frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        x = circle[0] #x position of centre in mm
        y = circle[1] #y position of centre in mm
        err,point_cloud_value = point_cloud.get_value(x,y) #GREY SCALE IMAGE DETECTION MAY NEED TO SCALE TO ZED CAMERAS SCALE
        distance = np.linalg.norm(np.array([point_cloud_value[0],point_cloud_value[1],point_cloud_value[2]]))
        print("Retroreflector position - ({point_cloud_value[0]},{point_cloud_value[1]},{point_cloud_value[2]})")
        print("Distance - {distance}")
        
zed.close()
cv2.destroyAllWindows()
