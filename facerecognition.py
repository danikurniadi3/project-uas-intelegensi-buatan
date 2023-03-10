# ===========================================
# Face Detection using Cascade Classifier
# ===========================================
import cv2

face_cascade = cv2.CascadeClassifier("haarcascade.xml")
img = cv2.imread('tes0.jpg')
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

wajah = face_cascade.detectMultiScale(
    gray_img,
    scaleFactor = 1.316,
    minNeighbors = 2
)

print(wajah)
print(type(wajah))

# ===========================================
# menambahkan kotak deteksi di area wajah
# ===========================================

for x, y, w, h in wajah:
    img = cv2.rectangle(
        img,            # image object
        (x,y),          # posisi kotak
        (x+w, y+h),     # posisi kotak
        (0, 255, 0),    # warna kotak RGB
        2               # lebar garis kotak
    )

resized = cv2.resize(img, (800,600))
cv2.imshow('Deteksi wajah', resized)
cv2.imwrite('tes1.jpg', resized)
cv2.waitKey(0)
cv2.destroyAllWindows()