# attendence_project

The whole project contains files:
- button_input.py
- recognise_image_model_prototype.py
- recognise_prototype.py
- face_recognition_project(main)

the former 3 files contain the prototype code(basic outline of the working) adb the latter directory
contains the main 3 files:
- attendence.txt
- dataset_faces.dat
- detector.py
- rec.jpg
- recognisor.py
- test.py
- train_images

The dataset_faces.dat file contains all the encodings of the faces present in train_images folder,
the encodings are appended by the file recognisor.py. When the detector.py is excecuted it first
loads all the encodings from the .dat file and takes a picture stores it in the rec.jpg and fianlly 
compares the encodings of the captured face to those of the known faces. Finally, if known image is 
detected, it appends the name to the attendence.txt file
