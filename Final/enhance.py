import cv2

def enhance_image(image_path):
    image_file = f"{image_path}"
    img = cv2.imread(image_file)
    def grayscale(image):
        return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray_image = grayscale(img)
    cv2.imwrite("temp/gray.jpg", gray_image)
    th = cv2.adaptiveThreshold(gray_image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 
                                            cv2.THRESH_BINARY, 139, 5) 
    enhanced_image_path = image_path.replace(".", "_enhanced.")
    cv2.imwrite(enhanced_image_path, th)
    return enhanced_image_path