import sqlite3 as sql
import os
import cv2
import face_recognition as fr
import json

conn = sql.connect('/Users/pa394538/attendance.db')
cursor = conn.cursor()
pathlib = 'UniqueImagesActors'
myList = os.listdir(pathlib)
images =[]
Names = []
i=0
print(myList)
for cl in myList:
    if not cl.startswith('.'):
        currImg = cv2.imread(f'{pathlib}/{cl}')
        images.append(currImg)
        name = os.path.splitext(cl)[0]
        roll_num = int(os.path.splitext(name)[0])
        # import pdb; pdb.set_trace()
        actual_name =os.path.splitext(name)[1]
        real_name = actual_name.replace('.', '')
        Names.append(real_name)
        encoding = fr.face_encodings(currImg)[0]
        item = [roll_num,real_name,currImg,json.dumps(encoding.tolist())]
        cursor.execute("INSERT INTO ATTENDANCE_SHEET (ROLL_NUM,NAME,PICTURE,FACE_ENCODING) VALUES (?, ?, ?, ?)", item)




conn.commit()
conn.close()


# conn.execute("UPDATE COMPANY set SALARY = 25000.00 where ID = 1")
# conn.execute("INSERT INTO ATTENDANCE_SHEET (ROLL_NUM,NAME,PICTURE,FACE_ENCODING) \
#       VALUES ({}, {}, {}, {})".format(os.path.splitext(cl)[0], currImg,   ));
