import face_recognition
import pickle
import os

all_face_encodings = {}
PATH = r"/home/pi/Desktop/programming/face recognition project/train_images"

for path in os.listdir(PATH):
    img = face_recognition.load_image_file("/home/pi/Desktop/programming/face recognition project/train_images/{}".format(path))
    all_face_encodings[path.split(".")[0]] = face_recognition.face_encodings(img)[0]

with open('/home/pi/Desktop/programming/face recognition project/dataset_faces.dat', 'wb') as f:
    pickle.dump(all_face_encodings)
    print("saved encodings")