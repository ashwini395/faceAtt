import cv2
import os
import face_recognition as fr
import numpy as np
from datetime import datetime
import sqlite3 as sql
import json

print("all required libraries loaded")

conn = sql.connect('/Users/pa394538/attendance.db')
cursor = conn.cursor()

LOL  = cursor.execute("SELECT NAME, FACE_ENCODING FROM ATTENDANCE_SHEET")
results = cursor.fetchall()
encodings = [np.asarray(json.loads(encoding[1])) for encoding in results]
names = [name[0] for name in results]


pathlib = 'UniqueImagesActors'


def Attendance(name):
    with open('Attendance_Register.csv','r+') as f:
        DataList = f.readlines()
        names = []
        for data in DataList:
            ent = data.split(',')
            names.append(ent[0])
        if name not in names:
            curr = datetime.now()
            dt = curr.strftime('%H:%M:%S')
            f.writelines(f'\n{name},{dt}')


# encodeKnown = DbEncodings(images)
print('Encoding Complete')



cap = cv2.VideoCapture(0)
print(cap.isOpened())

while True:
    _, img = cap.read()
    image = cv2.resize(img,(0,0),None,0.25,0.25)
    rgb_small_frame = image[:, :, ::-1]
    cv2.imshow('lol', rgb_small_frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


    # import pdb; pdb.set_trace()


    # image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    facesInFrame = fr.face_locations(rgb_small_frame)
    encodesInFrame = fr.face_encodings(rgb_small_frame,facesInFrame)


    for encodeFace,faceLoc in zip(encodesInFrame,facesInFrame):
            print("hello")
            matchList = fr.compare_faces(encodings,encodeFace)
            faceDist = fr.face_distance(encodings,encodeFace)
            match = np.argmin(faceDist)
            if matchList[match]:
                name = names[match].upper()
                print(name)
                Attendance(name)
