from picamera import PiCamera
import face_recognition
import numpy as np
import pickle
from time import sleep
import RPi.GPIO as gpio

gpio.setwarnings(False)
gpio.setmode(gpio.BOARD)

no_of_matches = 0
button = 11
led = 7

gpio.setup(button, gpio.IN, pull_up_down = gpio.PUD_DOWN)
gpio.setup(led, gpio.OUT)
gpio.output(led, gpio.LOW)

with open('/home/pi/Desktop/programming/face recognition project/dataset_faces.dat', 'rb') as f:
	all_face_encodings = pickle.load(f)

names = list(all_face_encodings.keys())
print(names)
face_encodings = np.array(list(all_face_encodings.values()))

cam = PiCamera()
cam.resolution = (852, 480)

print("ready...")
try:
	while True:
		if gpio.input(button) == 1:
			gpio.output(led, gpio.HIGH)
			print("started")
			cam.start_preview()
			sleep(3)

			cam.capture("rec.jpg")
			cam.stop_preview()

			gpio.output(led, gpio.LOW)

			unknown_image = face_recognition.load_image_file("/home/pi/Desktop/programming/face recognition project/rec.jpg")
			unknown_face = face_recognition.face_encodings(unknown_image)
			try:
				result = face_recognition.compare_faces(face_encodings, unknown_face)
			except ValueError:
				print("face not detected")
				continue

			names_with_result = list(zip(names, result))
			with open("attendence.txt", "a") as file:
				for data in names_with_result:
					if data[1] == True:
							print(data[0], "present")
							file.write("\n {}:present".format(data[0]))
			print("ready...")

except KeyboardInterrupt:
	gpio.cleanup()
	cam.stop_preview()

