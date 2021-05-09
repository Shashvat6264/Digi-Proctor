# :computer:Digi-Proctor
## :pushpin:Introduction
Students tend to take advantage of the online learning paradigm by indulging in short cut tricks to score more in exams. The project basically fosters a new standard of academic integrity by the detection of delinquency and malpractices in online assessments and hence securing the examination procedure of the e-learning paradigm. The project mainly focuses on the eradication of cheating in online examinations using checks like face detection and window checking.

## :construction:Working Project:construction:
**A working Video of the Project**  
[![VIDEO OF PROJECT](http://img.youtube.com/vi/6TFENvtDOok/0.jpg)](http://www.youtube.com/watch?v=6TFENvtDOok "FrostHack Project 'Digi-Proctor' Team 'We_Code'")  
The video explains the working of the project as well as all its technicalities. It also gives us a User Experience for both User Types, Professor as well as Teacher.

## How to Use:question:
To use the application one must have Python 3.8 or above version installed in their machine.

### :arrow_forward:Steps to Run:running: the project
1. Clone the repository in your machine.
2. Open a terminal in the repository root folder.
3. Install dependencies for the project from the requirements.txt file by using the command. 
```bash
pip install -r requirements.txt
```
4. Since, a database file is provided in the repository, you can directly run the Django server by the command: 
```bash
python3 manage.py runserver
```
5. If in any case the Database gets damaged, deleted or changed, you must migrate the already existing migrations to a new database. Command to migrate models to a new database is: 
```bash
python3 manage.py migrate
```
6. You can return to step 4 i.e. running the server, after doing migrations.
7. After running the server, go to the URL **"127.0.0.1:8000"** to see the app running.
8. You can test the app now.:confetti_ball::tada:

## :bookmark_tabs:Reasons to Use
Reasons to Use Digi-Proctor for examinations:
1. Remote Supervision and Proctoring
2. It is highly scalable, very reliable, extremely secure, and provides enhanced productivity
3. Digiproctor guarantees reliability by incorporating unique features at the student-end and in the back-end.
4. In proctored tests, the student is authenticated through facial analysis and is continually monitored during the test. Every non-compliant action is logged, and students' Trust Score is reduced.

## :scroll:Detailed Features
Our project aims to prevent students from performing malpractices by keeping a series of checks on the students throughout the course of the quiz. :zap:![Detailed Document Of the Project!](https://docs.google.com/document/d/15iE3nayH2szOoUU5ZPn-oNTuflI0lRAN7xjgVjxIm2o/edit?usp=sharing)
### :woman:**Face Detection**
The project makes the student feel like sitting in an examination room by giving them an online automated proctor who has his eyes on the student for the entire time. Our system uses face detection techniques to keep tabs on all of the activities of students throughout the exam. In case of detected malpractice, the system reports to the professor with an analysis. 
### :mag:**Window Changing**
During the course of the exam, one must not refer to the internet hence, we introduce a listener who detects if the student has changed his/her window in the machine. The count of how many times he/she has changed the screen is reported and above a certain threshold, the student is blacklisted and reported to the professor.
### :clock1:**Time-taken per Question**
The application also keeps tabs on how much time is taken by a student per question and a full analysis report is generated for each student. This analysis report is provided to the professor as an extra precaution to check for possible malpractice.

## :rocket:Challenges Faced
Some challenges that we ran into include:
1. :boy:**Face Detection**: Detecting the face of the student was a very big challenge and we resolved this challenge by using the *HaarCascade XML* file to detect the face of the student taking the exam. The video with the detected face still needed some processing namely putting text and boxing the detected face. This was achieved by using the frameworks *OpenCV* and *Numpy*.
2. :video_camera:**Streaming the video to FrontEnd**: Even after receiving the processed feed, there was a problem in streaming it to the FrontEnd of the website. This issue was overcome by using a constant URL where the video feed was streamed. This URL was used as the source URL in the image tag of the FrontEnd hence, the processed image was successfully streamed to the portal.
3. :chart:**Counting and Timing the time of Window Change**: Another problem we faced was counting and timing the window change during the quiz done by the student. We got past this issue by using built-in functions in JavaScript and then sending the collected information to the Django server by sending a *POST* request from JavaScript to the server.
4.  :key:**User Authentication**: We aimed for developing the project for multiple user types namely Student and Professor. This was a very difficult challenge for us which was overcome by using Proxy Models for Student and Professor, which inherited a Custom User built by us. We further went on to develop a Login Page that detects the type of User and responds with the corresponding layout of the website. This was achieved by creating a dummy URL *"/dashboard"* that recognized the User type from its attributes and then redirected the webpage to the corresponding dashboard.

## :dart:Future Scope
It was always said that :star2:Digitalization:star2: is the future, this Pandemic made the statement come true and completely drove life online. The current situation has led to an inevitable surge in the use of digital technologies. The web app needs to be constantly updating with regard to addressing new malpractices introduced by students.  
:sparkling_heart:Our team has come up with the idea of a dynamic online examination software to uphold academic integrity with a more secure way of assessments. Our project supports the development of original thinking skills and helps students do their best, original work.  
Some :inbox_tray:suggestions for addition of features in the future includes:  
:blush:*Face Recognition* to verify identity of student and :microphone:*Audio Recognition* to verify that the student is not talking to other parties.:sparkles:

