import cv2
image_file = "temp/1.jpg"
img = cv2.imread(image_file)
def grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray_image = grayscale(img)
cv2.imwrite("temp/gray.jpg", gray_image)
th = cv2.adaptiveThreshold(gray_image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 
                                          cv2.THRESH_BINARY, 139, 5) 
cv2.imwrite("temp/bw.jpg", th)
