from tkinter import *
import os
import cv2
import numpy as np
from PIL import Image
from tkinter import messagebox
import xlwrite;
import time
from datetime import datetime;

#start=time.time()
#period=30
def dataset():
    global data_screen
    data_screen =Toplevel(main_screen)
    data_screen.title("Login")
    data_screen.geometry("300x250")
    Label(data_screen, text="Please enter details below to login").pack()
    Label(data_screen, text="").pack()

    global name_verify
    global rollno_verify

    name_verify = StringVar() #Defining name_verify datatyo
    rollno_verify = StringVar()

    global name_login_entry
    global rollno_login_entry

    Label(data_screen, text="Name * ").pack()
    name_login_entry = Entry(data_screen, textvariable=name_verify)
    name_login_entry.pack()
    Label(data_screen, text="").pack()
    Label(data_screen, text="Roll No  * ").pack()
    rollno_login_entry = Entry(data_screen, textvariable=rollno_verify)
    rollno_login_entry.pack()
    Label(data_screen, text="").pack()
    Button(data_screen, text="OK", width=10, height=1, command= taking_dataset or data_screen.destroy).pack()


def taking_dataset():

    cam = cv2.VideoCapture(0)  # capturing video by initializing camera
    cam.set(3, 640)  # for video width
    cam.set(4, 480)  # for video height
    face_detector = cv2.CascadeClassifier('Cascades/haarcascade_frontalface_default.xml')
    username1= name_verify.get()
    rollno1= rollno_verify.get()
    messagebox.showinfo("Information","Initializing face capture. Look the camera and wait ...")
    # Initialize individual sampling face count
    count = 0
    while (True):
        ret, img = cam.read()  # capture image frame and return value true or false
        img = cv2.flip(img, 1)  # used to rotate the screen optional -1 rotates screen certically
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # converting RGB to gray
        faces = face_detector.detectMultiScale(gray, 1.3, 5)  # some image may be closer than others so  detects all image
        for (x, y, w, h) in faces:  # corner points x y and width and height of detected face
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
            count += 1
            # Save the captured image into the datasets folder
            cv2.imwrite("dataset/User." + str(rollno1) +'.'+ str(username1) + '.' + str(count) + ".jpg", gray[y:y + h, x:x + w])
            cv2.imshow('image', img)  # draws the rectangle of the detected face
        k = cv2.waitKey(100) & 0xff  # used for 64 bit machine  anding to get 8 bit
        if k == 27:  # Press 'ESC' for exiting video
            break
        elif count >= 60:  # Take 60 face sample and stop video
            break

    cam.release()
    cv2.destroyAllWindows()
    training_datasets()




def training_datasets():
    path = 'dataset'  # Path for face image database
    recognizer = cv2.face.LBPHFaceRecognizer_create()  # creates a recognizer to train recognizing datasets
    detector = cv2.CascadeClassifier("Cascades/haarcascade_frontalface_default.xml");
    # function to get the images and label data
    def getImagesAndLabels(path):
        imagePaths = [os.path.join(path, f) for f in os.listdir(path)]
        faceSamples = []  # list to hold sampled faces
        ids = []  # list to hold ids
        for imagePath in imagePaths:
            PIL_img = Image.open(imagePath).convert('L')  # convert it to grayscale
            img_numpy = np.array(PIL_img, 'uint8')
            id = int(os.path.split(imagePath)[-1].split(".")[1])
            faces = detector.detectMultiScale(img_numpy)
            for (x, y, w, h) in faces:
                faceSamples.append(img_numpy[y:y + h, x:x + w])  # add image to list of image
                ids.append(id)  # add id to list of ids
        return faceSamples, ids

    messagebox.showinfo("Information","Training faces. It will take a few seconds. Wait ...")
    faces, ids = getImagesAndLabels(path)
    recognizer.train(faces, np.array(ids))  # trains the faces using the datasets
    # Save the model into trainer/trainer.yml
    recognizer.write('trainer/trainer.yml')
    # Print the numer of faces trained and end program
    print("\n [INFO] {0} faces trained. Exiting Program".format(len(np.unique(ids))))


def take_attendance():
    start=time.time()
    period=12
    recognizer = cv2.face.LBPHFaceRecognizer_create()  # create lpbh face recognizer
    recognizer.read('trainer/trainer.yml')
    cascadePath = "Cascades/haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(cascadePath);
    font = cv2.FONT_HERSHEY_SIMPLEX
    # iniciate id counter
    id = 0
    names = [' ', 'Manoj', 'Ram', 'Srijana', 'Sanjay']
    # Initialize and start realtime video capture
    cam = cv2.VideoCapture(0)
    cam.set(3, 640)  # set video width
    cam.set(4, 480)  # set video height
    # Define min window size to be recognized as a face
    minW = 0.1 * cam.get(3)
    minH = 0.1 * cam.get(4)
    while True:
        ret, img = cam.read()
        img = cv2.flip(img, 1)  # Flip vertically
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.2,
            minNeighbors=5,
            minSize=(int(minW), int(minH)),
        )
        for (x, y, w, h) in faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
            ids, confidence = recognizer.predict(gray[y:y + h, x:x + w])
            if (confidence < 60):
                id = names[ids]
                confidence = "  {0}%".format(round(100 - confidence))
                filename=xlwrite.output('attendance','class1',ids,id,'yes');
				
            else:
                id = "unknown"
                confidence = "  {0}%".format(round(100 - confidence))

            cv2.putText(img, str(id), (x + 5, y - 5), font, 1, (255, 255, 255), 2)
            cv2.putText(img, str(confidence), (x + 5, y + h - 5), font, 1, (255, 255, 0), 1)

        cv2.imshow('camera', img)
        k = cv2.waitKey(10) & 0xff
        if k==27:
            break;
        if time.time()>start+period:
            break;
    print("\n [INFO] Exiting Program ")
    cam.release()
    cv2.destroyAllWindows()



def see_attendance():
    os.startfile(os.getcwd()+"/firebase/attendance_files/attendance"+str(datetime.now().date())+'.xls')
	#os.get return cureent working directory
	#os.startfile starts 

def xyz():
    messagebox.showinfo("Information","This option is in working stage!! ")

def main_account_screen():
    global main_screen
    main_screen = Tk()
    main_screen.geometry("500x400")
    main_screen.title("Account Login")
    Label(text="Select Your Choice", bg="blue", width="300", height="3", font=("Calibri", 13)).pack()
    Label(text="").pack()#for gap
    Button(text="Take data", height="2",bg="green", width="30", command=dataset).pack()
    Label(text="").pack()
    Button(text="Take attendance", height="2",bg="green", width="30", command=take_attendance).pack()
    Label(text="").pack()
    Button(text="See attendance", height="2",bg="green", width="30", command=see_attendance).pack()
    Label(text="").pack()
    Button(text="About developer", height="2",bg="green" ,width="30", command=xyz).pack()
    Label(text="").pack()
    Button(text="Exit", height="2", width="30",bg="green", command=main_screen.destroy).pack()
    main_screen.mainloop()


main_account_screen()
