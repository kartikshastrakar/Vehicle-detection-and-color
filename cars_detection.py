# OpenCV Python program to detect cars in video frame
# import libraries of python OpenCV
import cv2

# capture frames from a video
cap = cv2.VideoCapture('30_Minutes_of_Cars_Driving_By_in_2009(360p).mp4')

# Trained XML classifiers describes some features of some object we want to detect
car_cascade = cv2.CascadeClassifier('cars.xml')

# loop runs if capturing has been initialized.
while True:
	# reads frames from a video
	ret, frames = cap.read()
	
	# convert to gray scale of each frames
	gray = cv2.cvtColor(frames, cv2.COLOR_BGR2GRAY)
	

	# Detects cars of different sizes in the input image
	cars = car_cascade.detectMultiScale(gray, 1.1, 1)
	
	# To draw a rectangle in each cars
	for (x,y,w,h) in cars:
		cv2.rectangle(frames,(x,y),(x+w,y+h),(0,0,255),2)


    # Program Termination
	cv2.imshow("Multiple Color Detection in Real-TIme",frames )
	if cv2.waitKey(10) & 0xFF == ord('q'):
		cap.release()
		cv2.destroyAllWindows()
		break
  
     