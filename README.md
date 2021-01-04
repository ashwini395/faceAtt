# faceAtt
Face Attendance Recognition

- download and install Anaconda  from https://www.anaconda.com/products/individual

- wget -c https://repo.anaconda.com/archive/Anaconda3-2020.11-MacOSX-x86_64.sh (mac Os)

- chmod 755 Anaconda3-2020.11-MacOSX-x86_64.sh

- ./Anaconda3-2020.11-MacOSX-x86_64.sh

- conda init

- conda create -n <env_name>

- conda activate <env_name>

- conda install -y pandas

- conda install -y numpy

- conda istall -y scipy

- conda install -y opencv

- conda install -c conda-forge face_recognition

- conda install -c anaconda sqlite

#create DB

- sqlite3 attendance.db

#### then create table in attendance.db

- CREATE TABLE ATTENDANCE_SHEET(
   ROLL_NUM INT PRIMARY KEY NOT NULL,
   NAME TEXT    NOT NULL,
   PICTURE IMAGE NOT NULL,
   FACE_ENCODING BLOB   
);


# Generate encodings

- python generate_encodings.py

# run and test 


- python test.py
