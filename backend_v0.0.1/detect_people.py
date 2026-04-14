import cv2
import matplotlib.pyplot as plt

def detectPeople(img):
    if img is None:
        print("Error: Could not load image. Please check the file path and ensure the image exists.")
    else:
        plt.imshow(img)
        # plt.show()
    
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,  # Compensates for faces at different distances
        minNeighbors=5,   # Defines how many neighbors each candidate rectangle should have
        minSize=(30, 30)  # Minimum possible object size
    )
    
    print("Detected Peoples:",len(faces))
    return(faces)

def displayDetectedFaces(img,faces):
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
    plt.imshow(img)
    plt.show()
    
if __name__ == "__main__":
    img = cv2.imread("image0.png")
    plt.imshow(img)
    faces = detectPeople(img)
    displayDetectedFaces(img,faces)