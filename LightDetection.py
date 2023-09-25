import cv2
import numpy as np

# Create a VideoCapture object to capture the camera feed
cap = cv2.VideoCapture(0)  # 0 represents the default camera, you can change this value if you have multiple cameras

while True:
    # Read a frame from the camera
    ret, frame = cap.read()

    if not ret:
        print("Failed to capture frame from camera.")
        break

    # Convert the frame to grayscale
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Set pixel values below 250 to 0
    gray_frame[gray_frame < 240] = 0

    # Detect circles using Hough Circle Transform
    circles = cv2.HoughCircles(
        gray_frame, cv2.HOUGH_GRADIENT, dp=1, minDist=50, param1=30, param2=15, minRadius=10, maxRadius=100
    )

    if circles is not None:
        circles = np.uint16(np.around(circles))
        
        for circle in circles[0, :]:
            # Draw the outer circle
            cv2.circle(gray_frame, (circle[0], circle[1]), circle[2], (0, 255, 0), 2)
            # Draw the center of the circle
            cv2.circle(gray_frame, (circle[0], circle[1]), 2, (0, 0, 255), 3)
            
            # Print the coordinates of the center of the circle
            print(f"Circle Center: X = {circle[0]}, Y = {circle[1]}")

    # Display the modified grayscale frame with detected circles
    cv2.imshow("Circle Detection", gray_frame)
    #print(circle[0])
    # Break the loop if the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close the OpenCV windows
cap.release()
cv2.destroyAllWindows()
